# -*- coding: utf-8 -*- 

import re
import urllib2
import pandas as pd 
#获取原码
def get_content(page):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
    url ='http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'+ str(page)+'.html'
    req = urllib2.Request(url,headers=headers)  
    res = urllib2.urlopen(req)  
    html = res.read() 
    re= unicode(html, "gbk").encode("utf8")
    return re

def get(html):
    reg = re.compile(r'class="t1 ">.*? href="(.*?)".*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
    items=re.findall(reg,html)
    return items

def info_get(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
    req = urllib2.Request(url,headers=headers)  
    res = urllib2.urlopen(req)  
    html = res.read() 
    html = unicode(html, "gbk").encode("utf8")
    reg = re.compile(r'<span class="sp4"><em class="(.*?)"></em>(.*?)</span>',re.S)
    based_info = re.findall(reg,html)
    reg_p = re.compile(r'<span class="el">(.*?)</span>',re.S)
    kind = re.findall(reg_p,html)
    return based_info,kind

def address(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}
    req = urllib2.Request(url,headers=headers)  
    res = urllib2.urlopen(req)  
    html = res.read() 
    html = unicode(html, "gbk").encode("utf8")
    reg_a = re.compile(r'<div class="tBorderTop_box bmsg">.*?</span>(.*?)</p>',re.S)
    address = re.findall(reg_a,html)
    return address   

final = []
for  j in range(1,2):
    print("正在爬取第"+str(j)+"页数据...")
    try:
        html=get_content(j)
        for i in get(html):
            result = {}
            with open ('51job.txt','a') as f:
                f.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\t'+i[4]+'\t'+i[5]+'\t'+i[6]+'\n')
                f.close()
            result['info_link'] = i[0]
            info,kind = info_get(i[0])
            count = 1
            for n in info:
                if count == 1:
                    result['experience'] = n[1]
                    count += 1
                elif count == 2:
                    result['educational'] = n[1]
                    count += 1
                else:
                    break
            result['work_type'] = kind[0]
            result['address'] = address
            result['name'] = i[1]
            result['company'] = i[2]
            result['company_link'] = i[3]
            result['work_place'] = i[4]
            result['salary'] = i[5]
            ad = address(i[3])
            result['address'] = ad
            result['publish_time'] = i[6]
            final.append(result)
    except:
        pass
df = pd.DataFrame(final)  
df.to_csv('51job-data_analysis.csv', mode = 'a',encoding = 'utf8')





