#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib2

url = "http://www.lxa.kim"

#构建一个httphandler处理器对象，支持处理http请求
#http_handler = urllib2.HTTPHandler()

http_handler = urllib2.HTTPHandler(debuglevel=1)
#创建调试信息

#调用build_opener方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request(url)
response = opener.open(request)
print response.read()