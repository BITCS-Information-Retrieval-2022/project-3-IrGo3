# -*- codeing = utf-8 -*-
# @Author: youchaoZhou
# @File  :acl_crawler.py
# @Software: PyCharm

'''
爬虫思路：
1、爬取网页
2、解析数据
3、保存数据

'''

from bs4 import BeautifulSoup
import re
import urllib
import requests
import os
import pandas as pd
import sys
import random
import time
import json

# acl网站中有jsp的动态内容;

class Crawler_Paper():
    '''ACL官网爬虫类'''
    def __init__(self):
        '''
            构建基础的信息
        '''
        self.aclroot='https://aclanthology.org'
        self.base_url = 'https://aclanthology.org/volumes/2022.acl-long/' # 基础的url
        self.filepath='./ACL'
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"} 
        # request header
        self.paper_num = 1
        self.pdflist=[]
        self.htmllist=[]
        self.data = pd.DataFrame()    # 用于保存文献信息
        # self.template={
        #         "id": "007-democratically-finding-the-cause-of",
        #         "arxiv_id": "1802.07222",
        #         "nips_id": None,
        #         "url_abs": "http://arxiv.org/abs/1802.07222v1",
        #         "url_pdf": "http://arxiv.org/pdf/1802.07222v1.pdf",
        #         "title": "007: Democratically Finding The Cause of Packet Drops",
        #         "abstract": "Network failures continue to plague datacenter operators as their symptoms\nmay not have direct correlation with where or why they occur. We introduce 007,\na lightweight, always-on diagnosis application that can find problematic links\nand also pinpoint problems for each TCP connection. 007 is completely contained\nwithin the end host. During its two month deployment in a tier-1 datacenter, it\ndetected every problem found by previously deployed monitoring tools while also\nfinding the sources of other problems previously undetected.",
        #         "authors": [],
        #         "published": "2018-02-20",
        #         "video_url":"test"
        # } #我们只有id,url_abs,url_pdf,title,abstract,authors,video_url这几项;
        self.template={
                "id": "null",
                "arxiv_id": "null",
                "url_abs": "null",
                "url_pdf": "null",
                "title":"null",
                "abstract": "null",
                "authors": "null",
                "published": "null",
                "video_url":"null"
        }

    def get_page(self, url, write=True):
        '''
        获取网页信息函数，发送请求，获取响应内容
        :param url: 需要进入的网址
        :return req.text: 返回解码后的网页信息
        '''

        # 多次爬取则休眠，避免被对方反爬到
        time.sleep(random.randint(5,10))
        # req = requests.get(url, headers=self.header, params=params)

        # 如果是用Request库
        # 返回解码后的内容：requests.get().text
        # 返回字节：requests.get().content
        # return req.text

        req = urllib.request.Request(url=url, headers=self.header)
        response=urllib.request.urlopen(req).read()
        if write:
            name=url.split("/")[-2] # url是.../name/
            filename=os.path.join(self.filepath,"{}.html".format(name))
            self.htmllist.append(filename)
            with open(filename,"wb") as fh:   # 将文件写入到当前目录中
                fh.write(response)
        self.content=response.decode("utf-8")
        return response.decode("utf-8")
        # 可以用参数&pn=0,pn=10,pn=20分别访问到第1,2,3页

    def start(self):
        '''执行爬虫,包括请求,获取内容,解析网页,获取关键信息'''

        print('爬虫开始...')
        # 创建存储信息的文件夹
        try:
            os.makedirs(self.filepath)
        except FileExistsError:  # 如果文件夹已经存在，则跳过
            pass
        # new_url = self.input_message(self.base_url) # 构建网页查询的url,get请求构造参数
        new_url="https://aclanthology.org/volumes/2022.acl-long/"
        content = self.get_page(url=new_url) # 返回网页内容

        # print(content)
        # self.analyze_page(content) #解析网页,获取相关内容
        # self.data.to_excel(self.filepath, index=False) #将内存数据保存为excel
    
    def analyze_mainpage(self,content=""):
        '''
            analyze every years' ACL-long papers mainpage 
        '''
        if content=="":
            content=self.content
        bs=BeautifulSoup(content,"html.parser")
        entries=bs.find_all(name="p", attrs={"class" :"d-sm-flex align-items-stretch"})
        
        pagelist=[]
        for entry in entries:
            entry=entry.find_all(name="span", attrs={"class" :"d-block"})[1] # 为什么把class内含有d-block的也找出来了..
            detailed=entry.find("a",attrs={"class" :"align-middle"})
            if detailed["href"]:
                pagelist.append(detailed["href"])
        self.paper_num =len(pagelist)
        print("We have {} papers in 2022 year's ACL-long".format(len(pagelist)))
        self.pagelist=pagelist
        return pagelist

    def gethtml_local(self,url=""):
        '''
            reload the html file for detailed parsing
        '''
        if url=="":
            url=os.path.join(self.filepath,"test.html")
        with open(url,"rb") as fh:   # 将文件写入到当前目录中
            lines=fh.readlines()
        content=""
        for line in lines:
            content=content+line.decode("utf-8")
        self.content=content
        return content
    
    def analyze_details(self,content):
        '''
            get the detailed description of each essay
            get the pdf's url of each page
        '''
        bs=BeautifulSoup(content,"html.parser")
        itemdicts={}
        for key,value in self.template.items():
            itemdicts[key]=value

        # 标题,作者,摘要;
        abs=bs.find(name="div", attrs={"class" :"card-body acl-abstract"})
        itemdicts["abstract"]=abs.find(name="span").contents[0].text
        
        titletag=bs.find(name="h2", attrs={"id" :"title"}).contents[0]
        title=""
        for items in titletag:
            while hasattr(items,"contents"):
                items=items.contents[0].text
            if (type(items)!=str):
                title+=items.text
            else:
                title+=items
        itemdicts["title"]=title

        authortag=bs.find(name="p", attrs={"class" :"lead"})
        authors=[]
        for items in authortag:
            if hasattr(items,"contents"):
                authors.append(items.contents[0].text)
        itemdicts["authors"]=" ".join(authors)


        # id,pdf_url,page_url,video_url
        table=bs.find(name="dl")
        tags=table.find_all(name="dt")
        tagcontents=table.find_all(name="dd")
        for idx,entry in enumerate(tags):
            item=entry.contents[0]
            if item =="PDF:":
                self.pdflist.append(tagcontents[idx].contents[0]["href"])
                itemdicts["url_pdf"]=tagcontents[idx].contents[0]["href"]
            elif item =="Anthology ID:":
                itemdicts["id"]=tagcontents[idx].contents[0].text
            elif item=="URL:":
                itemdicts["url_abs"]=tagcontents[idx].contents[0]["href"]
            elif item=="Video:":
                itemdicts["video_url"]=tagcontents[idx].contents[0]["href"]
        for value in itemdicts.values():
            if (type(value)!=str):
                print(type(value),value)
        return itemdicts

    def download_pdf(self,size=1024):
        '''
            download every pdf in pdflist
        '''
        count=0
        time.sleep(random.randint(2,5))
        for url in self.pdflist:       
            try:
                r=requests.get(url,stream=True)
                filename=url.split("/")[-1]

                with open(os.path.join(self.filepath,filename),"wb") as fd:
                    for chunk in r.iter_content(chunk_size=size):
                        fd.write(chunk)
                
            except:
                print("Unexpected Error in Network for idx:{}".format(count))
            count+=1

def main():
    '''调用自定义爬虫类Crawler_Paper'''
    crawler = Crawler_Paper()
    # crawler.start()
    crawler.gethtml_local()
    pagelist=crawler.analyze_mainpage()
    # get the detailed page
    count=0
    for item in pagelist[540:]:
        url=crawler.aclroot+item
        content=crawler.get_page(url)
        # content=crawler.gethtml_local("./ACL/2022.acl-long.1.html")
        # crawler.analyze_details(content)
        count+=1
        if count  % 20==0 :
            print("Having processed {} pages".format(count))
    print(len(crawler.pdflist))
    # crawler.download_pdf()

if __name__=='__main__':
    root="./ACL"
    video_count=0
    toparse=os.listdir(root)
    crawler = Crawler_Paper()
    aclurls="2022acl.json"
    aclcorpus=[]
    for file in toparse:
        filepath=os.path.join(root,file)
        content=crawler.gethtml_local(filepath)
        entry=crawler.analyze_details(content)
        aclcorpus.append(entry)
        if entry["video_url"] != "null":
            video_count+=1
    print("video_count:",video_count)
    with open(aclurls,"w") as fw:
        json.dump(aclcorpus,fw)
   
    



