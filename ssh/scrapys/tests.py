#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
from bs4 import BeautifulSoup
import urllib2
import urllib
import json    # 使用了json格式存储
 
  
  
url = 'http://api.map.baidu.com/geocoder/v2/'  
output = 'json'  
ak = 'Nv9tbmYPkwWvohzEo8tAsSPt5xYPi0DU'  
add='东湖高新区光谷大道光谷金融港B22栋-402室'  
uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak #百度地理编码API 
req = urllib2.Request(uri)  
req = urllib2.urlopen(req)   
res = req.read()
res = unicode(res, "gbk").encode("utf8") 
temp = json.loads(res)  
print(temp['result']['location']['lng'],temp['result']['location']['lat'])#打印出经纬度 