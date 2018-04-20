#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#date(2018-4-20)
import urllib2
import urllib

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
header = {  #^(.*):\s(.*)$
"Host" : "fanyi.youdao.com",
#"Connection" : "keep-alive",
#"Accept" : "application/json, text/javascript, */*; q=0.01",
#"Origin" : "http://fanyi.youdao.com",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400",
"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
# "Referer" : "http://fanyi.youdao.com/",
#"Accept-Encoding" : "gzip, deflate",
"Accept-Language" : "zh-CN,zh;q=0.8",
#"Cookie" : "OUTFOX_SEARCH_USER_ID=1810812697@10.168.8.64; _ntes_nnid=0db6a516923f02cd58686d05ec026211,1497244507535; P_INFO=matrixwzd@163.com|1508064896|2|mail163|00&99|sic&1508064349&carddav#sic&510100#10#0#0|&0|163&mailsettings&mail163|matrixwzd@163.com; OUTFOX_SEARCH_USER_ID_NCOO=1931040389.789685; JSESSIONID=aaaJD6cFAJKEjb-JrhHlw; ___rl__test__cookies=1524195350415"
# "Content-Length" : "217"
}

key = raw_input("请输入需要翻译的文字：")
formdata = {  #^(.*):(.*)$  "\1" : "\2"   通过WebForms查询
"i" : key,
"from" : "AUTO",
"to" : "AUTO",
"smartresult" : "dict",
"client" : "fanyideskweb",
"doctype" : "json",
"version" : "2.1",
"keyfrom" : "fanyi.web",
"action" : "FY_BY_REALTIME",
"typoResult" : "true"
}


formdata = urllib.urlencode(formdata)
request = urllib2.Request(url, data = formdata, headers = header)
response = urllib2.urlopen(request)

print response.read()