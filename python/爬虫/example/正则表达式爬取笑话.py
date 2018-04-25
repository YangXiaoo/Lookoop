#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# date(2018-4-21)
import urllib2
import urllib
import re
import sys

class Spider:
	'''
		网页爬虫简单通用型
	'''
	def load_page(self, url, page, filename):
		'''
			加载页面
		'''
		url = url + page 
		#print url
		header = {
			"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			#"Accept-Encoding" : "gzip, deflate, sdch, br",
			"Accept-Language" : "zh-CN,zh;q=0.8",
			"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400",
			"Connection" : "keep-alive"			
			}
		request = urllib2.Request(url, headers = header)
		response = urllib2.urlopen(request)
		res = response.read()
		#typeEncode = sys.getfilesystemencoding()
		#result = res.decode('utf-8','ignore').encode(typeEncode)
		result = res.decode('gbk', 'ignore').encode('utf-8')
		#print result
		#UnicodeDecodeError: 'gbk' codec can't decode bytes in position 1-2: illegal multibyte sequence
		#解决办法：忽略非法字符
		myfile = open('test.txt','w')
		myfile.write(result)
		myfile.close()
		reg = re.compile(r'<span id="text110">(.*?)</span>')
		html = reg.findall(result)			
		self.print_page(html, filename)

	def print_page(self, html, filename):
		'''
			显示内容
		'''
		print "正在显示内容..."
		for item in html:
			print item
			self.writePage(item,filename)
	def writePage(self, item, filename):
		'''
			写入本地
		'''
		print "存储内容..."
		with open(filename,'a') as f:
			f.write(item)
			f.write("\n\t")
			f.write("*"*20)
			f.close()
			print "存储成功"
		print "存储文件名：" + filename


if __name__ == '__main__':
	'''
		爬虫入口
	'''
	url = raw_input("请输入网址：")
	#http://www.jokeji.cn/jokehtml/%E5%86%B7%E7%AC%91%E8%AF%9D/2018032623300493.htm
	reg_url = url
	ispage = raw_input("是否有页码：[y/n]")
	if ispage.lower() == 'y':
		page = int(raw_input("请输入页码："))
	else:
		page = ""
	patten = re.compile(r'[a-z]+\.[a-z]+')
	res = patten.search(reg_url)
	filename = res.group() + ".txt"
	#print filename

	myspider = Spider()
	myspider.load_page(url, page, filename)
