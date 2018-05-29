#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import hashlib
import sys

def location(address): 
    url = 'http://api.map.baidu.com/geocoder/v2/'  
    output = 'json'   
    ad = address.encode("utf8")
    t="中文"
    ak = 'Nv9tbmYPkwWvohzEo8tAsSPt5xYPi0DU' 
    ad = str(ad)

    # address = address.encode("gbk") 


    uri = url + '?' + 'address=' + ad  + '&output=' + output + '&ak=' + ak


    req = urllib2.Request(uri)  
    req = urllib2.urlopen(req)   
    res = req.read()
    res = unicode(res, "gbk").encode("utf8") 
    temp = json.loads(res)
    lng = temp['result']['location']['lng']
    lat = temp['result']['location']['lat']
    return lat,lng

def changeCode(name):
    return name
