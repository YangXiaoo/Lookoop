#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import re
import urllib2
import pandas as pd 
def info_get(url=""):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
    url ='https://jobs.51job.com/all/co2272673.html'
    req = urllib2.Request(url,headers=headers)  
    res = urllib2.urlopen(req)  
    html = res.read() 
    html = unicode(html, "gbk").encode("utf8")
    reg = re.compile(r'<div class="tBorderTop_box bmsg">.*?</span>(.*?)</p>',re.S)
    items = re.findall(reg,html)
    print items
info_get()