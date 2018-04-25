import requests
from lxml import etree
from Queue import Queue
import threading
import time
import json

class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        #threading.Thread.__init__(self) #继承父类
        super(ThreadCrawl, self).__init__() #调用父类初始化方法
        #线程名
        self.threadName = threadName
        #页码队列
        self.pageQueue = pageQueue
        #数据队列
        self.dataQueue = dataQueue

        self.header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}

    def run(self):
        print "启动" + self.threadName
        while not CRAW_EXIT:
            #取出一个数字，先进先出
            #block可选参数，默认true
            #1.如果队列为空，block为true，就会进入阻塞状态，直到队列有新的数据
            #2。如果对列空，block为False的话，就会弹出一个queue.empty()异常
            try:
                page = self.pageQueue.get(False)
                url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'
                content = requests.get(url,headers = self.header)
                self.dataQueue.put(content)
            except:
                pass
        print "结束" + self.threadName

CRAW_EXIT = False
PARSE_EXIT = False


class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
    def run(self):
        while not PARSE_EXIT:
            try:   
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
    def parse(self):
        html = etree.HTML(html)
        result = html.xpath('//div[contains(@id,"qiushi_tag")]')
        for site in result:
            try:
                imgUrl = site.xpath('.//img/@src')[0]
                title = site.xpath('.//h2')[0].text
                content = site.xpath('.//div[@class="content"]/span')[0].text.strip()
                vote = None
                comments = None
                try:
                    vote = site.xpath('.//i')[0].text
                    comments = site.xpath('.//i')[1].text
                except:
                    pass
                result = {
                    'imgUrl': imgUrl,
                    'title': title,
                    'content': content,
                    'vote': vote,
                    'comments': comments,
                }
                self.filename.write(json.dumps(result, ensure_ascii=False).encode('utf-8') + "\n")


def main():
    pageQueue = Queue(10) #页码队列，表示10个页码
    for i in range(1,11):
        '''
        放入1~10个数字，先进先出
        '''
        pageQueue.put(i)

    #采集结果的数据列队，参数空表示不限制
    dataQueue = Queue()

    filename = open("duanzi.jsaon",'a')

    crawList = ["采集线程1","采集线程2","采集线程3"]

    threadcrawl = []
    for threadName in crawList:
        thread = ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start() #线程执行
        threadcrawl.append(thread)

    parseList = ["解析线程1","解析线程2","解析线程3"]
    threadparse = [] #解析三个解析线程
    for threadName in parseList:
        thread = threadParse(threadName, dataQueue, filename)
        thread.start()
        threadparse.append(thread)

    #等待pageQueue队列为空，也就是等待之间执行完毕
    while not pageQueue.empty():
        pass

    #如果pageQueue为空，采集线程退出循环
    global CRAW_EXIT
    CRAW_EXIT = True

    print "pageQueue为空"

    #阻塞
    for thread in threadcrawl:
        thread.join()
        print "1"

if __name__ == '__main__':
    main()

