#date(2018-4-17)

安装
----
【方法一】
[root]# yum -y install libxslt-devel pyOpenSSL python-lxml python-devel gcc
[root]# easy_install scrapy
[root]# cd /opt
[root]# git clone https://github.com/scrapy/scrapy.git
[root]# cd scrapy
[root]# python setup.py install
[root]# pip install --upgrade Scrapy  
[root]# pip install --upgrade pip  #上一步可能提示pip版本过低

【方法二】
#安装依赖
[root]# yum -y groupinstall "Development tools" 
[root]# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel --skip-broken
#安装python
[root]# cd /usr/local/src
[root]# wget https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tgz
[root]# tar -zxvf Python-3.5.5.tgz
[root]# cd Python-3.5.5/
[root]# ./configure --prefix=/usr/local/python3
[root]# make && make install
#创建Python3，pip3的软链接
[root]# ln -s /usr/local/python3/bin/python3 /usr/bin/python3
[root]# ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
#安装Scrapy
[root]# pip3 install scrapy
[root]# ln -s /usr/local/python3/bin/scrapy /usr/bin/scrapy
[root]# scrapy -v
[root]# scrapy shell http://www.lxxx.site/Tp5/public/home/index/index
>>> response.xpath('//div[@class="list-arc-item top"][1]/a/@href').extract()
['/Tp5/public/deta/linux/212']

XPath
----
$x('//p') #选择所有p元素
$x('//a/@href') #选择所有连接
$x('//img/@src[1]') #选择第一个图片链接，下脚标从1开始
$x('//div[@id="touch"]//text()') #id="touch"下所有文本

启动一个项目
-----------
[root]# scrapy startproject lxweb
[root]# cd lxweb
[root]# tree 
.
├── lxweb
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field 


class LxwebItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #primary fields
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    #Caculate fieds
    images = Field()
    location = Field()

    #goods fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

[root]# scrapy genspider basic web
.
├── lxweb
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   └── settings.cpython-35.pyc
│   ├── settings.py
│   └── spiders
│       ├── basic.py  #编写代码，若出错删除重新编写
│       ├── __init__.py
│       └── __pycache__
│           └── __init__.cpython-35.pyc
└── scrapy.cfg
[root]# vim lxweb/spiders/basic.py
import scrapy

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6']

    def parse(self, response):
        self.log("title: %s" % response.xpath(
        	'//*[@class="title"][1]/@title').extract())
        self.log("price: %s" % response.xpath(
        	'//*[@class="Total brand_col"][1]/text()').extract())
        self.log("description: %s" % "none")
        self.log("address: %s" % response.xpath(
        	'//*[@id="container_base"]/ul/li[1]/div[2]/p/i[3]/a/text()').extract())
        self.log("image_urls: %s" % response.xpath(
        	'//*[@id="container_base"]/ul/li[1]/div[1]/div/a/img/@src').extract())

[root]# scrapy crawl basic #运行爬虫
[root]# vim lxweb/spiders/basic.py
import scrapy
from lxweb.items import LxwebItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6']

    def parse(self, response):
    	item = LxwebItem()
        item['title'] = response.xpath(
        	'//*[@class="title"][1]/@title').extract()
        item['price'] = response.xpath(
        	'//*[@class="Total brand_col"][1]/text()').extract()
        item['description'] = "none"
        item['address'] = response.xpath(
        	'//*[@id="container_base"]/ul/li[1]/div[2]/p/i[3]/a/text()').extract()
        item['image_urls'] = response.xpath(
        	'//*[@id="container_base"]/ul/li[1]/div[1]/div/a/img/@src').extract()
        return item

[root]# scrapy crawl basic -o items.json #运行爬虫并保存指定格式.jl,.csv
[root]# vim lxweb/spiders/basic.py #重新编写
import scrapy
import socket
import urlparse
import datetime
from scrapy.loader import TtemLoader
from scrapy.loader.processors import MapCompose, Join
from lxweb.items import LxwebItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6']

    def parse(self, response):
    	"""
    	This function parses property page.
    	@url http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6
		@return items 1
		@scrapes title price description address image_urls
		@scrapes url project spider server date
    	"""
    	#create loader using the response
    	l = ItemLoader(item=LxwebItem(),response=response)

    	#Loader fields using Xpath expressions
    	l.add_xpath('title','//*[@class="title"][1]/@title',MapCompose(unicode.strip,unicode.title))
    	l.add_xpath('price','//*[@class="Total brand_col"][1]/text()',MapCompose(unicode.strip))
    	l.add_xpath('description','none')
    	l.add_xpath('address','//*[@id="container_base"]/ul/li[1]/div[2]/p/i[3]/a/text()',MapCompose(unicode.strip))
    	l.add_xpath('image_urls','//*[@id="container_base"]/ul/li[1]/div[1]/div/a/img/@src',MapCompose(lamda i: urlparse.urljoin(response.url,i)))
        
        #FIELD
        l.add_value('url',response.url)
        l.add_value('project',self.settings.get('BOT_NAME'))
        l.add_value('spider',self.name)
        l.add_value('server',socket.gethostname())
        l.add_value('date',datetime.datetime.now())

        return l.load_time()
[root]# scrapy genspinder -t crawl easy web  #实现双向爬取
[root]# vim lxweb/spiders/easy.py
#python3.5版本下,import MapCpmpose不能用，urlparse也不能引入模块
import scrapy
import socket
import urlparse
import datetime
from scrapy.loader import TtemLoader
from scrapy.loader.processors import MapCompose, Join
from lxweb.items import LxwebItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    start_urls = ['http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"pages-next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="levelList"]/li[2]/a'),
        callback='parse_item', follow=True),
    )

    def parse(self, response):
    	"""This function parses  property page.
    	@url http://www.taoche.com/all/?from=1293855&WT_KW=%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BA%A4%E6%98%93%E5%B8%82%E5%9C%BA%E4%BA%8C%E6%89%8B%E8%BD%A6
		@return items 1
		@scrapes title price description address image_urls
		@scrapes url project spider server date
    	"""
    	#create loader using the response
    	l = ItemLoader(item=LxwebItem(),response=response)

    	#Loader fields using Xpath expressions
    	l.add_xpath('title','//*[@class="title"][1]/@title',MapCompose(unicode.strip,unicode.title))
    	l.add_xpath('price','//*[@class="Total brand_col"][1]/text()',MapCompose(unicode.strip))
    	l.add_xpath('description','none')
    	l.add_xpath('address','//*[@id="container_base"]/ul/li[1]/div[2]/p/i[3]/a/text()',MapCompose(unicode.strip))
    	l.add_xpath('image_urls','//*[@id="container_base"]/ul/li[1]/div[1]/div/a/img/@src',MapCompose(lambda i: urlparse.urljoin(response.url,i)))

    	l.add_value('url',response.url)
    	l.add_value('project',self.settings.get('BOT_NAME'))
    	l.add_value('spider',self.name)
    	l.add_value('server',socket.gethostname())
    	l.add_value('date',datetime.datetime.now())

    	return l.load_time()
[root]# scrapy crawl easy -s CLOSESPIDER_ITEMCOUNT=90
