# -- coding: utf-8 --
import requests
import json
from queue import Queue
import threading
import time
#url = 'https://paperswithcode.com/api/v1/papers/'
datasets = []
num = 0 #爬取的总数
N = 100000
class Crawl_thread(threading.Thread):
    def __init__(self, thread_id, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        self.craw_spider()
    def craw_spider(self):
        while(True):
            if self.queue.empty():
                break
            page = self.queue.get()
            url = "https://paperswithcode.com/api/v1/papers/?page=" + str(page)
            headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'
                }
            try:
                textjson = json.loads(requests.get(url,headers=headers).text)
                results = textjson['results']
                UpdataList(results)
            except Exception as e:
                print(url)
                print(e)
                exit()

def UpdataList(results):
    #print('call')
    for result in results:
        datasets.append(result)
        global num
        num = num + 1
        if(num % 10000== 0):
            print(num)
            print(time.asctime( time.localtime(time.time()) ))
if __name__ == "__main__":

    pageQueue = Queue(10000+10)
    for page in range(1,10000):
        pageQueue.put(page)
    crawl_threads = []
    crawl_name_list = []
    for i in range(1,10):
        crawl_name_list.append('crawl_'+str(i))
    print('start')
    for thread_id in crawl_name_list:
        thread = Crawl_thread(thread_id,pageQueue)
        thread.start()
        crawl_threads.append(thread)
    while not pageQueue.empty():
        pass
    for t in crawl_threads:
        t.join()

    jsonstr = json.dumps(datasets)
    with open('paperwithcode1e5.json','w') as f:
        f.write(jsonstr)


    '''
    num = 0
    nxt = url
    while(num < N):
        cur_url = nxt
        textjson = json.loads(requests.get(cur_url).text)
        nxt = textjson['next']
        results = textjson['results']
        UpdataList(results)
        if num % 100 == 0:
            print(num)
    '''
    