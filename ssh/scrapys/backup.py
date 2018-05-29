# coding: utf-8
import unittest
import urllib2
import urllib
import re
import json 
import lxml
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd

from collections import Iterable
import os

from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.db.models import Q

from scrapys.models import *
from ssh.settings import BASE_DIR


def index(request):
    return render_to_response('scraps/index.html',locals,context_instance=RequestContext(request))

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
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
    items=re.findall(reg,html)
    return items


def fjob(request):
    old = Jobs.objects.all()
    #if request.method == "POST":
    file_path = os.path.join(BASE_DIR,'scrapys/final_result.xlsx')
    file = pd.read_excel(file_path)
    file = pd.DataFrame(file)
    rows = len(file)
    raw_data = {}
    '''
    data['first_city'] = file[0][0]
    data['first_data'] = file[1][0]
    data['second_city'] = file[0][1]
    data['second_data'] = file[1][1]
    data['third_city'] = file[0][2]
    data['third_data'] = file[1][2]
    data['forth_city'] = file[0][3]
    data['forth_data'] = file[1][3]
    data['five_city'] = file[0][4]
    data['five_data'] = file[1][4]
    data['sx_city'] = file[0][5]
    data['sx_data'] = file[1][5]
    data['se_city'] = file[0][6]
    data['se_data'] = file[1][6]
    data['ei_city'] = file[0][7]
    data['ei_data'] = file[1][7]
    data['ni_city'] = file[0][8]
    data['ni_data'] = file[1][8]
    data['ten_city'] = file[0][9]
    data['ten_data'] = file[1][9]
    datas = json.dumps(data)
    '''
    if old:
        pass
    '''
    else:
        for i in range(0, rows): 
            try:   
                raw_data = {}
                raw_data['company'] = file['company'][i]  
                raw_data['name'] = file['name'][i]  
                raw_data['city'] = file['work_place'][i]
                low_salary = file['low_salary'][i]
                high_salary = file['high_salary'][i]
                raw_data['low_salary'] = low_salary
                raw_data['high_salary'] = high_salary
                raw_data['avg_salary'] = float((high_salary+low_salary)/2)
            
                raw_data['low_exp'] = file['low_exp'][i]
                raw_data['high_exp'] = file['high_exp'][i]

                raw_data['educational'] = file['educational'][i]
                raw_data['address'] = file['address'][i]
                raw_data['work_type'] = file['work_type'][i]
                raw_data['company_link'] = file['company_link'][i]
                raw_data['info_link'] = file['info_link'][i] 
                raw_data['publish_time'] = file['publish_time'][i] 
                jobs = Jobs(raw_data)
                jobs.save 
            except:
                pass
    '''
    for i in old:
        result = Handles.objects.filter(company=i.company)
        if result:
            result.avg_salary += int(i.avg_salary) 
            result.iter_count += 1
            result.save()
        else:
            company = i.company
            city = i.city
            avg_salary = int(i.avg_salary)
            iter_count = 1
            p = Handles(title='python',company=company,city=city,avg_salary=avg_salary,iter_count=iter_count)
            p.save()
    handle = Handles.objects.all()
    for i in handle:
        company = i.company
        city = i.city
        avg_salary = i.avg_salary / i.iter_count
        iter_count = 1
        p = Handles(title='python',company=company,city=city,avg_salary=avg_salary,iter_count=iter_count)
        p.save()
    #p=Handles(title='python',company='company',city='city',avg_salary=2,iter_count=2)
    #p.save()
    result = Handles.objects.order_by("avg_salary")[0:10]
    return render_to_response('scrapys/fjob.html',locals(),context_instance=RequestContext(request))














#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import hashlib
import sys
import os
import pandas as pd

def location(): 
    file = pd.read_excel('final_result.xlsx')  
    file = pd.DataFrame(file) 
    url = 'http://api.map.baidu.com/geocoder/v2/'  
    output = 'json'   

    ak = 'Nv9tbmYPkwWvohzEo8tAsSPt5xYPi0DU' 

    # address = address.encode("gbk") 
    data = []
    row = len(file)
    for i in range(1,row):
        raw_data = {}
        ad = file['address'][i]
        ad = str(ad.encode("utf8"))
        uri = url + '?' + 'address=' + ad  + '&output=' + output + '&ak=' + ak
        raw_data['address'] = file['address']

        req = urllib2.Request(uri)  
        req = urllib2.urlopen(req)   
        res = req.read()
        res = unicode(res, "gbk").encode("utf8") 
        temp = json.loads(res)
        lng = temp['result']['location']['lng']
        lat = temp['result']['location']['lat']
        raw_data['lng'] = lng
        raw_data['lat'] = lat
        data.append(raw_data)
    lt = pd.DataFrame(data)  
    lt.to_excel('latitude.xlsx')  
    print("Successfully Saved My File!") 

def changeCode(name):
    return name
location()