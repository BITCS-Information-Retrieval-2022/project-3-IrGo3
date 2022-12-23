import json
import requests
from queue import Queue
import threading
import time

'''
每个page有10本书
搜索主页:https://www.ebooks.com/en-us/search/subject/?pageNumber=1&CountryCode=US&subjectId=13
'''
datasets = []
num = 0  # 爬取的总数


def Crawler(pageNum, crawlerNum):
    '''
    pageNum:爬去的页面数量
    crawlerNum:线程数量
    '''
    pageQueue = Queue(pageNum + 10)
    for page in range(1, pageNum + 1):
        pageQueue.put(page)
    crawl_threads = []
    crawl_name_list = []
    for i in range(1, crawlerNum):
        crawl_name_list.append('crawl_' + str(i))
    print('start')
    for thread_id in crawl_name_list:
        thread = Crawl_thread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)
    while not pageQueue.empty():
        pass
    for t in crawl_threads:
        t.join()
    jsonstr = json.dumps(datasets)
    with open('data_ebook.json', 'w') as f:
        f.write(jsonstr)


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
            url = 'https://www.ebooks.com/api/search/subject/?pageNumber=' + str(page) + '&CountryCode=US&subjectId=13'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'
            }
            try:
                results = json.loads(requests.get(url, headers=headers).text)['books']
                UpdataList(results)
            except Exception as e:
                print(url)
                print(e)
                exit()


def UpdataList(results):
    for result in results:
        datasets.append(result)
        global num
        num = num + 1
        if(num % 10000 == 0):
            print('num = ', num)
            print(time.asctime(time.localtime(time.time())))


if __name__ == "__main__":
    Crawler(
        pageNum=5000,
        crawlNum=10,
    )
