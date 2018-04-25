#date(2018-4-18)
爬虫设计思路：
	1.确定Url
	2.通过协议获取对应的html
	3.提取数据
		a.如果是需要的数据，保存
		b.如果有其它url，继续执行第二步

php对多线程，异步，支持不够好，并发处理能力弱,爬虫是工具性程序，对数据和效率要求比较高

解析服务器响应内容：re,xpath,beautifulsoup(bs4),jsonpath,pyquery
框架：(scrapy,pyspider)
	异步网络框架twisted,提供数据存储，数据下载，提取规则
分布式：scrapy-redis，主要在redis中做请求指纹去重(python中用set)，请求分配(列队push)，数据临时存储
爬虫-反爬虫-反反爬虫之间的斗争

通用爬虫
-------
搜索引擎用的爬虫系统。把互联网所有网页下载下来，放到本地服务器形成备份，针对网页做处理，为
用户提供一个借口。
爬虫协议：robot.txt跟在域名后面www.xxx.com/robot.txt

聚焦爬虫
-------
针对某种内容爬虫

HTTP:
基本格式：scheme://host[:port#]/path/…/[?query-string][#anchor]

scheme：协议(例如：http, https, ftp)
host：服务器的IP地址或者域名
port#：服务器的端口（如果是走协议默认端口，缺省端口80）
path：访问资源的路径
query-string：参数，发送给http服务器的数据
anchor：锚（跳转到网页的指定锚点位置）

抓包工具 telerik fiddler web debugger


urllib2
Python自带：/usr/local/python2.7/urllib2.py 
pip安装: /url/local/lib/python2.7/site-packages/item.py
[root]# vim url2.py
import urllib2

#浏览器代理，伪装
ua_list = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"
}

#通过urllib2.Request()方法构造请求对象
request = urllib2.Request("http://www.baidu.com",headers = ua_header)

request.add_header("Connection", "keep-alive")

# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)
# 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()

code = response.getcode() #返回http的响应码，成功返回200,4服务器页面，403重定向，5服务器

print response.geturl() #返回实际页面，防止重定向

print response.info()   #返回服务器响应报头

# 打印字符串
print html


###########################################
import urllib2
import random

url = "http://www.itcast.cn"

ua_list = [
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3177.0 Safari/537.36"
]

user_agent = random.choice(ua_list)

request = urllib2.Request(url)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("User-Agent", user_agent)

# 第一个字母大写，后面的全部小写
request.get_header("User-agent")

response = urllib2.urlopen(url)

html = response.read()
print html


url和url2
----------
urllib 和 urllib2 都是接受URL请求的相关模块，但是提供了不同的功能。两个最显著的不同如下：
	urllib 仅可以接受URL，不能创建 设置了headers 的Request 类实例；
	但是 urllib 提供 urlencode 方法用来GET查询字符串的产生，而 urllib2 则没有。（这是 urllib 和 urllib2 经常一起使用的主要原因）
	编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，解码工作可以使用urllib的unquote()函数。（注意，不是urllib2.urlencode() )
---------------------------------------------
# IPython2 中的测试结果
In [1]: import urllib

In [2]: word = {"wd" : "传智播客"}

# 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
In [3]: urllib.urlencode(word)  
Out[3]: "wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2"

# 通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
In [4]: print urllib.unquote("wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2")
wd=传智播客
---------------------------------------------------
手动搜索：
import urllib 
import urllib2
import random
url = "http://www.baidu.com/s"
ua_list = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400",
}

keyword = raw_input("请输入关键字：")
wd = {'wd':keyword}
wd = urllib.urlencode(wd)
url = url + "?" + wd 

request = urllib2.Request(url,headers = url_list)

#也可以通过调用Request.add_header() 添加/修改一个特定的header

reponse = urllib2.urlopen(request)

print reponse.read()



百度贴吧
tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0 
---------

if __name__=="__main__":
	kw = raw_input("请输入要爬取的贴吧：")
	beginPage = int(raw_input("请输入起始页码："))
	endPage = int(raw_input("请输入终止页码:"))

	url = "http://tieba.baidu.com/f?"

	key = urllib.urlencode({"kw":kw})

	url = url + key 
	tiebaSpider(url, beginPage, endPage)




post
----
{
    "translateResult":[
        [
            {
                "tgt":"fruit",
                "src":"水果"
            }
        ]
    ],
    "errorCode":0,
    "type":"zh-CHS2en",
    "smartResult":{
        "entries":[
            "",
            "fruits "
        ],
        "type":1
    }
}
i=%E6%B0%B4%E6%9E%9C%0A  #i=水果
from=AUTO
to=AUTO
smartresult=dict
client=fanyideskweb
salt=1524195350415
sign=ad68f9a43181e27db807a087a11cba14
doctype=json
version=2.1
keyfrom=fanyi.web
action=FY_BY_REALTIME
typoResult=false

XML(EXtensible Markup Language)
-------------------------------
XML的设计宗旨是传输数据，标签需要自定义，被设计为具有自由描述性


beautifulsoup4
-------------
是一个HTML/XML的解析器，但是速度慢

计算机的核心CPU，一个CPU只能执行一个任务
一个CPU一次只能执行一个进程
进程的执行单元叫线程，一个进程可以包含多个线程。
一个进程的内存空间是共享的，每个进程里的线程都可以使用这个共享空间。
一个线程在使用这个共享的时候，其它线程必须等它结束

通过锁实现，防止多个线程使用这个空间。

进程：表示程序的一次执行
线程：CPU运算的基本调度单位

GIL：python里的执行通行证，而且只有一个，

python的多线程适用于大量密集的I/O处理，文件处理
python多进程适用于大量的密集并行计算

[root]# pip install selenuim 
[root]#wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
[root]# tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
