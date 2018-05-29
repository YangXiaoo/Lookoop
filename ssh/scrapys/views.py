# -*- coding: utf-8 -*- 
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
from ssh.api import get_object

from scrapys.api_sp import *

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
    #if request.method == "POST":
    file_ = os.path.join(BASE_DIR,'scrapys/final_result.xlsx')
    file_ = pd.read_excel(file_)
    file = pd.DataFrame(file_)
    rows = len(file)
    raw_data = {}
    old = Job.objects.filter(company=file['company'][1])
    '''
    if not old:
        for i in range(1, rows):               
            raw_data = {}
            company = changeCode(file['company'][i]) 
            name = changeCode(file['name'][i])  
            city = changeCode(file['city'][i])
            low_salary = changeCode(file['low_salary'][i])
            high_salary = changeCode(file['high_salary'][i])
            avg_salary = (float(high_salary)+ float(low_salary))/2            
            low_exp = changeCode(file['low_exp'][i])
            high_exp = changeCode(file['high_exp'][i])
            educational = file['educational'][i]
            address = changeCode(file['address'][i])
            work_type = changeCode(file['work_type'][i])
            company_link = changeCode(file['company_link'][i])
            info_link = changeCode(file['info_link'][i]) 
            publish_time = changeCode(file['publish_time'][i])

            jobs = Job(name=name,company=company,educational=educational,city=city,low_salary=low_salary,high_salary=high_salary,low_exp=low_exp,avg_salary=avg_salary,high_exp=high_exp,address=address,company_link=company_link,info_link=info_link,work_type=work_type,publish_time=publish_time)
            jobs.save()
    '''

    new = Job.objects.all()
    '''
    # handle for location
    n = 1
    for k in new:
        url = 'http://api.map.baidu.com/geocoder/v2/'  
        output = 'json'   
        ad = file['address'][n].encode("utf8")
        ad = str(ad)
        ak = 'Nv9tbmYPkwWvohzEo8tAsSPt5xYPi0DU' 
        # address = address.encode("gbk") 
        uri = url + '?' + 'address=' + ad  + '&output=' + output + '&ak=' + ak

        req = urllib2.Request(uri)  
        req = urllib2.urlopen(req)   
        res = req.read()
        res = unicode(res, "gbk").encode("utf8") 
        temp = json.loads(res)
        lng = temp['result']['location']['lng']
        lat = temp['result']['location']['lat']
        k.lng = lng 
        k.lat =lat
        k.save()
        n += 1
    '''
    '''
    for i in new:
        result = Handle.objects.filter(city=i.city)
        if result:
            for result in result:
                result.avg_salary = float(result.avg_salary)+float(i.avg_salary)
                result.iter_count = int(result.iter_count)+1
                result.iter_count=result.iter_count
                result.save()
        else:
            city = i.city
            avg_salary = float(i.avg_salary)
            iter_count = 1
            p = Handle(title='python',city=city,avg_salary=avg_salary,iter_count=iter_count)
            p.save()

    handle_re = Handle.objects.all()
    for i in handle_re :
        i.avg_salary = float(i.avg_salary) / int(i.iter_count)
        i.save()
    '''
    top_sa = Handle.objects.order_by("-avg_salary")[0:10]
    x_sa = []
    y_sa = []
    for h in top_sa:
        x_sa.append(h.city)
        plc = h.avg_salary.find('.')
        y_sa.append(h.avg_salary[:plc+2])
    x_sa = json.dumps(x_sa)
    y_sa = json.dumps(y_sa)    
    '''
    # handle for TopCity
    for t in new:
        top_city = get_object(TopCity, city=t.city)
        if top_city:
                top_city.avg_salary = float(top_city.avg_salary)+float(t.avg_salary)
                top_city.iter_count = int(top_city.iter_count)+1
                top_city.save()
        else:
            city = t.city
            avg_salary = float(t.avg_salary)
            iter_count = 1
            title = 'python'
            p = TopCity(title=title,city=city,avg_salary=avg_salary,iter_count=iter_count)
            p.save() 
    '''
    new_city = TopCity.objects.order_by("-iter_count")[0:10]
    x_ct = []    
    y_ct = []
    for h in new_city:
        x_ct.append(h.city)
        y_ct.append(h.iter_count)
    x_ct = json.dumps(x_ct)
    y_ct = json.dumps(y_ct)

    city_list = []
    title = ['score', 'amount', 'product']
    city_list.append(title)
    for h in new_city:
        tmp = []
        avg_salary = str(float(h.avg_salary)/(float(h.iter_count)))
        plc = avg_salary.find('.')
        tmp.append(avg_salary[:plc+2])
        tmp.append(h.iter_count)
        tmp.append(h.city)
        city_list.append(tmp)
    city_high = city_list[1][0]
    city_low = city_list[10][0]
    city_list = json.dumps(city_list)       

    '''
    # handle for educational
    handle_edu = Job.objects.all()
    for i in handle_edu:
        result = get_object(Edu, educational=i.educational)
        if result:           
            result.total_salary = float(result.total_salary)+float(i.avg_salary)
            result.iter_count = int(result.iter_count)+1
            result.save()
        else:
            educational = i.educational
            total_salary = float(i.avg_salary)
            iter_count = 1
            title = 'python'
            p = Edu(title=title,educational=educational,total_salary=total_salary,iter_count=iter_count)
            p.save()
    edu_re = Edu.objects.all()
    for i in edu_re :
        i.total_salary = float(i.total_salary) / int(i.iter_count)
        i.save()
    '''
    edu = Edu.objects.all()
    edu_list = []
    edu_title = []
    for e in edu:
        edu_data = {}
        edu_data['value'] = e.iter_count
        edu_data['name'] = e.educational
        edu_list.append(edu_data)
        edu_title.append(e.educational)

    edu_data = json.dumps(edu_data)
    edu_title = json.dumps(edu_title)
    edu_list = json.dumps(edu_list)
    '''
    # handle for WorkType
    for i in new:
        result = get_object(WorkType, work_type=i.work_type)
        if result:           
            result.total_salary = float(result.total_salary)+float(i.avg_salary)
            result.iter_count = int(result.iter_count)+1
            result.save()
        else:
            work_type = i.work_type
            total_salary = float(i.avg_salary)
            iter_count = 1
            title = 'python'
            p = WorkType(title=title,work_type=work_type,total_salary=total_salary,iter_count=iter_count)
            p.save()
    '''
    wk_tp = WorkType.objects.all()
    wk_list = []
    wk_title = []
    for e in wk_tp:
        wk_data = {}
        wk_data['value'] = e.iter_count
        wk_data['name'] = e.work_type
        wk_list.append(wk_data)
        wk_title.append(e.work_type)

    wk_title = json.dumps(wk_title)
    wk_list = json.dumps(wk_list)


    '''
    # handle for experience
    for i in new:
        result = get_object(WorkExp, exp=i.low_exp)
        if result:           
            result.total_salary = float(result.total_salary)+float(i.avg_salary)
            result.iter_count = int(result.iter_count)+1
            result.save()
        else:
            exp = i.low_exp
            total_salary = float(i.avg_salary)
            iter_count = 1
            title = 'python'
            p = WorkExp(title=title,exp=exp,total_salary=total_salary,iter_count=iter_count)
            p.save()
    '''
    exp = WorkExp.objects.order_by("exp")
    leng = len(exp)
    if leng < 8:
        exp = exp[:leng]
    else:
        exp = exp[:8]
        leng = 8
    exp_list = []
    exp_title = []
    for e in exp:
        exp_data = {}
        exp_data['value'] = e.iter_count
        exp_data['name'] = str(e.exp) + '年工作经验'
        title = str(e.exp) + '年工作经验'
        exp_list.append(exp_data)
        exp_title.append(title)
        #exp_list.reverse()
    exp_max = exp_list[0].get('value')
    exp_min = exp_list[leng-1].get('value')
    exp_title = json.dumps(exp_title)
    exp_list = json.dumps(exp_list)

    exp_x = []
    exp_y = []
    exp = WorkExp.objects.order_by("exp")
    for e in exp:
        ep = str(e.exp) + '年'
        exp_x.append(ep)
        avg_salary = str(float(e.total_salary)/(float(e.iter_count)))
        plc = avg_salary.find('.')
        exp_y.append(avg_salary[:plc+2])
    exp_x = json.dumps(exp_x)
    exp_y = json.dumps(exp_y)

    return render_to_response('scrapys/fjob.html',locals(),context_instance=RequestContext(request))