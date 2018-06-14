#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import hashlib
import sys

import re
import pandas as pd 
from ssh.settings import *

def location(address): 
    url = 'http://api.map.baidu.com/geocoder/v2/'  
    output = 'json'   
    ak = 'Nv9tbmYPkwWvohzEo8tAsSPt5xYPi0DU' 
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
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

class Scrapy(object):
    '''
    爬取数据，40页，两层结构
    共请求1640个页面
    应考虑使用线程
    '''
    def __init__(self,title):
        self.title = title
        self.file_name = os.path.join(BASE_DIR,'scrapys/files/', title + "_data_analysis.csv")
        self.data_name = os.path.join(BASE_DIR,'scrapys/files/', title+ '.txt')

    @staticmethod
    def get_content(page,title):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8'}
        url ='http://search.51job.com/list/000000,000000,0000,00,9,99,'+ str(title) +',2,'+ str(page)+'.html'
        req = urllib2.Request(url, headers=headers)  
        res = urllib2.urlopen(req)  
        html = res.read() 
        re= unicode(html, "gbk").encode("utf8")
        return re

    @staticmethod
    def get(html):
        reg = re.compile(r'class="t1 ">.*? href="(.*?)".*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
        items=re.findall(reg,html)
        return items

    @staticmethod
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

    @staticmethod
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


    def get_data(self):
        final = []
        for j in range(1,50):
            try:
                html = self.get_content(j,self.title)
                for i in self.get(html):
                    result = {}
                    with open (self.data_name,'a') as f:
                        f.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\t'+i[4]+'\t'+i[5]+'\t'+i[6]+'\n')
                        f.close()
                    result['info_link'] = i[0]
                    info,kind = self.info_get(i[0])
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
                    # result['address'] = self.address
                    result['name'] = i[1]
                    result['company'] = i[2]
                    result['company_link'] = i[3]
                    result['work_place'] = i[4]
                    result['salary'] = i[5]
                    ad = self.address(i[3])
                    result['address'] = ad
                    result['publish_time'] = i[6]
                    final.append(result)
            except:
                pass
        df = pd.DataFrame(final)  
        df.to_csv(self.file_name, mode = 'a',encoding = 'utf8')
        return self.file_name,self.data_name


class HandleData(object):
    '''
    处理爬虫数据，过滤，分离。返回excel文件名，返回过滤后的文件名
    '''
    def __init__(self, title, file_name):
        self.title = title
        self.data_tran = os.path.join(BASE_DIR,'scrapys/files/', title + '_tran.xlsx')
        self.file_name = file_name
        self.data_final = os.path.join(BASE_DIR,'scrapys/files/', title + '_final.xlsx')
        self.clean_data = []
  
    def select_dataposition(self):  
        data = pd.read_csv(self.file_name, header = 0, encoding= 'utf8')  
        df = pd.DataFrame(data)  
        df.to_excel(self.data_tran)

    def get_file_elements(self):  
        file = pd.read_excel(self.data_tran)  
        file = pd.DataFrame(file)  
        rows = len(file)  
        for i in range(0, rows): 
            try: 
                raw_data = {}  
                raw_data['company'] = file['company'][i]  
                raw_data['name'] = file['name'][i]  
                if '-' in file['work_place'][i]:  
                    plc_1 = file['work_place'][i].find('-')  
                    raw_data['city'] = file['work_place'][i][:plc_1]  
                else:  
                    raw_data['city'] = file['work_place'][i]  
                    # print(file['salary'][i])  
                if file['salary'][i] == "":  
                    raw_data['low_salary'] = ''  
                    raw_data['high_salary'] = ''  
                elif '-' in file['salary'][i]:  
                    plc_2 = file['salary'][i].find('-')  
                    low_salary = file['salary'][i][:plc_2]  
                    high_salary = file['salary'][i][plc_2 + 1 :].encode("utf8").rstrip('万/月|千/月|万/年|天')  
                    if '万/月' in file['salary'][i].encode("utf8"):  
                        raw_data['low_salary'] = float(low_salary) * 10  
                        raw_data['high_salary'] = float(high_salary) * 10  
                    elif '千/月' in file['salary'][i].encode("utf8"):  
                        raw_data['low_salary'] = float(low_salary)  
                        raw_data['high_salary'] = float(high_salary)  
                    elif '万/年' in file['salary'][i].encode("utf8"):  
                        raw_data['low_salary'] = float(low_salary) * 10 / 12  
                        raw_data['high_salary'] = float(high_salary) * 10 / 12
                    elif '天' in file['salary'][i].encode("utf8"):
                        raw_data['low_salary'] = float(low_salary) * 30
                        raw_data['high_salary'] = float(high_salary) * 30  
                elif '天' in file['salary'][i].encode("utf8"):
                    raw_data['low_salary'] = float(low_salary) * 30
                    raw_data['high_salary'] = float(high_salary) * 30
                elif '时' in file['salary'][i].encode("utf8"):
                    continue
                elif '以' in file['salary'][i].encode("utf8"):
                    continue
                else:
                    raw_data['low_salary'] = file['salary'][i]
                    raw_data['high_salary'] = file['salary'][i]
                if '-' in file['experience'][i].encode("utf8"):  
                    plc_2 = file['experience'][i].find('-')  
                    raw_data['low_exp'] = file['experience'][i][:plc_2]  
                    raw_data['high_exp'] = file['experience'][i][plc_2 + 1 :].encode("utf8").rstrip('年经验')
                elif '无工作经验' in  file['experience'][i].encode("utf8"):
                    raw_data['high_exp'] = 0  
                    raw_data['low_exp'] = 0
                else:
                    raw_data['high_exp'] = file['experience'][i].encode("utf8").rstrip('年经验')  
                    raw_data['low_exp'] = file['experience'][i].encode("utf8").rstrip('年经验')
                raw_data['info_link'] = file['info_link'][i]
                if '(' in  file['address'][i]:
                    plc_2 = file['address'][i].find('(') 
                    raw_data['address'] = file['address'][i][:plc_2].strip('[\[\]]')
                elif '筛选' in file['address'][i]:
                    continue
                elif not file['address'][i]:
                    continue
                elif len(file['address'][i])>200:
                    continue
                else:
                    raw_data['address'] = file['address'][i].strip('[\[\]]')
                raw_data['work_type'] = file['work_type'][i]
                if '招' in file['educational'][i].encode("utf8"):
                    raw_data['educational'] = 0
                else:
                    raw_data['educational'] = file['educational'][i] 
                raw_data['company_link'] = file['company_link'][i]  
                raw_data['publish_time'] = file['publish_time'][i]

                # In case of error:'ascii' codec can't decode byte ... in position ...: ordinal not in range(128)
                # self.fh.write("""<si><t%s>%s</t></si>""" % (attr, string))
                try: 
                    test = """%s %s %s %s %s %s %s %s %s %s %s %s %s"""  % (raw_data['company'],raw_data['name'],raw_data['city'],raw_data['address'],raw_data['work_type'],raw_data['educational'],raw_data['company_link'],raw_data['publish_time'],raw_data['info_link'],raw_data['low_exp'],raw_data['high_exp'],raw_data['low_salary'],raw_data['high_salary'])
                except:
                    continue

                self.clean_data.append(raw_data)  
            except Exception,e:
                pass
        return self.clean_data

    def save_clean_data(self):  
        lt = pd.DataFrame(self.clean_data)  
        lt.to_excel(self.data_final)  
    
    def get_result(self):  
        self.select_dataposition() 
        clean_data = self.get_file_elements() 
        self.save_clean_data() 

        return self.data_tran,self.data_final 
