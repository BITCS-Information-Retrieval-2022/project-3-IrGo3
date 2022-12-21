import requests
import json
import re
import time
from lxml import etree
from faker import Factory
from threading import Thread, Lock
requests.packages.urllib3.disable_warnings()


class Crawler:

    def __init__(self, path):
        self.datasets = []
        self.hashset = set()
        self.set_lock = Lock()
        self.path = path

    def crawl(self, keywords):
        for keyword in keywords:
            paper = keyword
            video_url = f'https://api.bilibili.com/x/web-interface/search/all/v2?context=&page=1&order=&keyword={paper}'
            has = False
            for _ in range(60):
                res = requests.get(
                    video_url, headers={'User-Agent': Factory.create().user_agent()},
                    stream=True, verify=False, timeout=(60, 60)
                )
                if res.status_code == 200:
                    has = True
                    res = res.json()
                    break
            if not has:
                continue
            try:
                for data in res['data']['result'][-1]['data']:
                    self.set_lock.acquire()
                    if data["bvid"] not in self.hashset:
                        self.hashset.add(data["bvid"])
                        self.datasets.append({
                            "bvid": data["bvid"],
                            "title": ''.join(re.split('<em class=\"keyword\">|</em>', data['title'])),
                            "description": data["description"],
                            "tag": data["tag"],
                            "rank_score": data["rank_score"],
                            "play": data["play"],  # 播放
                            "like": data["like"],  # 点赞
                            "favorites": data["favorites"],  # 收藏
                            "danmaku": data["danmaku"],  # 弹幕
                            "paper": paper
                        })
                    self.set_lock.release()
            except KeyError:
                print(paper)

    def run(self, multi=True):
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
    crawler = Crawler('./allpapers.json')
    crawler.run()
