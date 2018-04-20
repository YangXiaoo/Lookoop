#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib2
import urllib
url = "http://www.lxxx.site/idng.html"

request = urllib2.Request(url)

try:
	urllib2.urlopen(request)
except urllib2.HTTPError, err:
	print err.code 
except urllib2.URLError, err:
	print err 
else:
	print "good job."