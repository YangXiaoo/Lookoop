# from bs4 import BeautifulSoup
# from selenium import webdriver
# import subprocess as sp
# from lxml import etree
import requests
import random
import re

class testData(object):
	def __init__(self):
		
S = requests.Session()
# http://222.197.182.137/redir.php?catalog_id=6&cmd=learning&tikubh=1484&page=2
catalog_id, tikubh, page = 6,1484,2
url = 'http://222.197.182.137/redir.php?catalog_id=%d&cmd=learning&tikubh=%d&page=%d' % (catalog_id, tikubh, page)
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'wsess=2oo18l9gpd4k6olqiu5laa5em1',
'Host':'222.197.182.137',
'Referer':'http://222.197.182.137/redir.php?catalog_id=121',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36',}
#get请求
target_response = S.get(url = url, headers = headers)
#utf-8编码
target_response.encoding = 'gbk'
#获取网页信息
target_html = target_response.text
print(target_html)