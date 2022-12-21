import time
import json
from random import randint
import requests
from lxml import etree
from faker import Factory
from threading import Thread, Lock
requests.packages.urllib3.disable_warnings()


class Crawler:

    def __init__(self, path):
        self.datasets = []
        self.hashset = set()
        self.set_lock = Lock()
        self.root = 'https://www.slideserve.com'
        self.path = path

    def crawl(self, keywords):
        for keyword in keywords:
            paper = keyword
            res = requests.get(
                '{}/search/presentations/{}'.format(self.root, paper.replace(' ', '-')),
                headers={'User-Agent': Factory.create().user_agent()},
                stream=True, verify=False, timeout=(60, 60)
            )
            html = res.text
            tree = etree.HTML(html)
            elements = tree.xpath("//div[@class='col-md-3 height-fix']/a/@href")
            for element in elements[:5]:
                self.set_lock.acquire()
                if element not in self.hashset:
                    self.hashset.add(element)
                    res = requests.get(
                        f'{self.root}{element}',
                        headers={'User-Agent': Factory.create().user_agent()},
                        stream=True, verify=False, timeout=(60, 60)
                    )
                    html = res.text
                    tree = etree.HTML(html)
                    try:
                        title = tree.xpath("/html/body/section/div/div[2]/div[1]/div/div[2]/h1/text()")
                        title = "None." if len(title) == 0 else title[0]
                        views = int(tree.xpath(
                            "/html/body/section/div/div[2]/div[1]/div/div[2]/div[1]/span[1]/text()"
                        )[0].split(' ')[1])
                        desc = tree.xpath("//*[@id='navpills-1']/p/text()")
                        desc = "None." if len(desc) == 0 else desc[0]
                    except (IndexError, AttributeError, ValueError) as e:
                        print(paper, f'{self.root}{element}', e)
                        self.set_lock.release()
                        continue
                    self.datasets.append({
                        'url': element,
                        'title': title,
                        'views': views,
                        'desc': desc,
                        'paper': paper
                    })
                self.set_lock.release()

    def run(self, multi=True):
        # with open(self.path, 'r', encoding='utf-8') as f:
        #     data = json.load(f)
        # keywords = [f"{row['authors'][0]['author_name']} {row['title']}" for row in data]
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        keywords = [f"{row['title']}" for row in data]
        tic = time.time()
        if multi:
            num, tot = 128, len(keywords)
            tl = []
            for i in range(0, num):
                t = Thread(
                    target=self.crawl, kwargs={"keywords": [keywords[j] for j in range(tot) if j % num == i]}, daemon=True
                )
                t.start()
                tl.append(t)
            for t in tl:
                t.join()
        else:
            self.crawl(keywords)
        print(f'datasets size = {len(self.datasets)}')
        with open('slideserve_paper2.json', 'w', encoding='utf-8') as f:
            json.dump(self.datasets, f, ensure_ascii=False)
        print(time.time() - tic)


if __name__ == "__main__":
    # crawler = Crawler('./ebook_cs_990.json')
    crawler = Crawler('./allpapers.json')
    crawler.run()
