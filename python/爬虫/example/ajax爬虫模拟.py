#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import urllib2
import urllib

url = "http://www.lxxx.site/Tp5/public/home/index/more/?"

page = int(raw_input("请输入查询页码："))
formdata = {'pages': page}
formdata = urllib.urlencode(formdata)

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}

request = urllib2.Request(url, data = formdata, headers = header)
response = urllib2.urlopen(request)

print response.read()