#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#date(2018-4-20)
import urllib2
import urllib


# http://tieba.baidu.com/f?kw=网页&ie=utf-8&pn=50
def load_page(url,filename):
	'''
		作用：根据url发送请求，获取响应文件
		url:需要爬取的url地址
	'''
	print "正在下载" + filename
	header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}
	request = urllib2.Request(url, headers = header)
	response = urllib2.urlopen(request)
	print filename + "下载成功!"
	return response.read()

def writePage(html,filename):
	'''
		作用：将html文件写入本地
		html:服务器响应文件内容
	'''
	print "正在存储" + filename
	with open(filename, 'w') as f:
		f.write(html)
		print "*" * 20
	print filename + "存储成功!"

def tiebaSpider(url, pageStart, pageEnd):
	'''
		作用：调度器传入url地址
		ps:起始页
		pe:结束页
	'''
	for page in range(pageStart,pageEnd + 1):
		pn = (pageStart - 1) * 50
		url = url +"pn="+ str(pn)
		filename = "第" +str(page)+ "页.html"

		html = load_page(url, filename)
		writePage(html, filename)

if __name__ == '__main__': 
	'''
		作用：直接运行该文件时才运行
	'''
	kw = raw_input("请输入爬取贴吧名称：")
	pageStart = int(raw_input("请输入起始页码："))
	pageEnd = int(raw_input("请输入结束页码："))

	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({"kw":kw})
	url = url + key 
	tiebaSpider(url, pageStart, pageEnd) 
else:
	print "不能引用该模块"