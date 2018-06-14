# -*- coding: utf-8 -*- 
# date(2018-5-24)
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
    if request.GET.get('keyword', ''):
        search_name = request.GET.get('keyword', '')
        data_ = search_name
        datas = get_object(AnsysFile,title=data_)
        if not datas:
            try:
                scrapys = Scrapy(search_name)
                file_name,data_name = scrapys.get_data()

                handles = HandleData(search_name, file_name)
                data_tran,data_final = handles.get_result()

                file = AnsysFile(title=data_,data_analy=file_name,data_txt=data_name,data_tran=data_tran,data_final=data_final)
                file.save()

                datas = get_object(AnsysFile,title=data_)
                file_path = pd.read_excel(datas.data_final)
                file = pd.DataFrame(file_path)
                rows = len(file)
                raw_data = {}

                old = Job.objects.filter(company=file['company'][2],title=data_)

                # save in table Job
                for i in range(1, rows):
                    try:               
                        raw_data = {}
                        title = data_
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

                        jobs = Job(name=name,title=title,company=company,educational=educational,city=city,low_salary=low_salary,high_salary=high_salary,low_exp=low_exp,avg_salary=avg_salary,high_exp=high_exp,address=address,company_link=company_link,info_link=info_link,work_type=work_type,publish_time=publish_time)
                        jobs.save()
                    except:
                        continue

                new = Job.objects.filter(title=search_name)

                # handle for location
                '''
                # unicode can't tranfer to string, and it will cause Bad Request
                n = 1
                for k in new:
                    lat,lnt = location(k.address.encode("unicode-escape").decode("utf8"))
                    k.lng = lng 
                    k.lat =lat
                    k.save()
                    n += 1
                '''

                # handle for top salary
                for i in new:
                    result = get_object(Handle,city=i.city,title=data_)
                    if result:
                        result.avg_salary = float(result.avg_salary)+float(i.avg_salary)
                        result.iter_count = int(result.iter_count)+1
                        result.iter_count=result.iter_count
                        result.save()
                    else:
                        city = i.city
                        avg_salary = float(i.avg_salary)
                        iter_count = 1
                        p = Handle(title=data_,city=city,avg_salary=avg_salary,iter_count=iter_count)
                        p.save()

                handle_re = Handle.objects.filter(title=data_)
                for i in handle_re :
                    i.avg_salary = float(i.avg_salary) / int(i.iter_count)
                    i.save()

                # handle for TopCity
                for t in new:
                    top_city = get_object(TopCity, city=t.city, title=data_)
                    if top_city:
                            top_city.avg_salary = float(top_city.avg_salary)+float(t.avg_salary)
                            top_city.iter_count = int(top_city.iter_count)+1
                            top_city.save()
                    else:
                        city = t.city
                        avg_salary = float(t.avg_salary)
                        iter_count = 1
                        title = data_
                        p = TopCity(title=title,city=city,avg_salary=avg_salary,iter_count=iter_count)
                        p.save() 

                # handle for educational
                for i in new:
                    result = get_object(Edu, educational=i.educational,title=data_)
                    if result:           
                        result.total_salary = float(result.total_salary)+float(i.avg_salary)
                        result.iter_count = int(result.iter_count)+1
                        result.save()
                    else:
                        educational = i.educational
                        total_salary = float(i.avg_salary)
                        iter_count = 1
                        title = data_
                        p = Edu(title=title,educational=educational,total_salary=total_salary,iter_count=iter_count)
                        p.save()
                edu_re = Edu.objects.all()
                for i in edu_re :
                    i.total_salary = float(i.total_salary) / int(i.iter_count)
                    i.save()

                # handle for WorkType
                for i in new:
                    result = get_object(WorkType, work_type=i.work_type, title=data_)
                    if result:           
                        result.total_salary = float(result.total_salary)+float(i.avg_salary)
                        result.iter_count = int(result.iter_count)+1
                        result.save()
                    else:
                        work_type = i.work_type
                        total_salary = float(i.avg_salary)
                        iter_count = 1
                        title = data_
                        p = WorkType(title=title,work_type=work_type,total_salary=total_salary,iter_count=iter_count)
                        p.save()

                # handle for experience
                for i in new:
                    result = get_object(WorkExp, exp=i.low_exp, title=data_)
                    if result:           
                        result.total_salary = float(result.total_salary)+float(i.avg_salary)
                        result.iter_count = int(result.iter_count)+1
                        result.save()
                    else:
                        exp = i.low_exp
                        total_salary = float(i.avg_salary)
                        iter_count = 1
                        title = data_
                        p = WorkExp(title=title,exp=exp,total_salary=total_salary,iter_count=iter_count)
                        p.save()

            except Exception,e:
                error = "爬取出错，联系站长<br>"
            datas = AnsysFile.objects.all()
            return render_to_response('scrapys/index.html',locals(),context_instance=RequestContext(request))
    else:
            datas = AnsysFile.objects.all()
            return render_to_response('scrapys/index.html',locals(),context_instance=RequestContext(request))

def fjob(request):
    if request.GET.get('keyword', 'python'):
        search_name = request.GET.get('keyword', 'python')
        new = Job.objects.all()
        # top 10 salary
        top_sa = Handle.objects.filter(title=search_name).order_by("-avg_salary")[0:10]
        x_sa = []
        y_sa = []
        for h in top_sa:
            x_sa.append(h.city)
            plc = h.avg_salary.find('.')
            y_sa.append(h.avg_salary[:plc+2])
        x_sa = json.dumps(x_sa)
        y_sa = json.dumps(y_sa)    

        # top 10 city
        new_city = TopCity.objects.filter(title=search_name).order_by("-iter_count")[0:10]
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

        # education requirement
        edu = Edu.objects.filter(title=search_name)
        edu_list = []
        edu_title = []
        for e in edu:
            edu_data = {}
            edu_data['value'] = e.iter_count
            if e.educational == '0':
                edu_data['name'] = '不限'
                e.educational = '不限'
            else:
                edu_data['name'] = e.educational
            edu_list.append(edu_data)
            edu_title.append(e.educational)

        edu_data = json.dumps(edu_data)
        edu_title = json.dumps(edu_title)
        edu_list = json.dumps(edu_list)

        # work type
        wk_tp = WorkType.objects.filter(title=search_name).order_by("-iter_count")[0:10]
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

        # work experience requirement
        exp = WorkExp.objects.filter(title=search_name).order_by("exp")
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

        # work experience for salary
        exp_x = []
        exp_y = []
        exp = WorkExp.objects.filter(title=search_name).order_by("exp")
        for e in exp:
            ep = str(e.exp) + '年'
            exp_x.append(ep)
            avg_salary = str(float(e.total_salary)/(float(e.iter_count)))
            plc = avg_salary.find('.')
            exp_y.append(avg_salary[:plc+2])
        exp_x = json.dumps(exp_x)
        exp_y = json.dumps(exp_y)

        return render_to_response('scrapys/fjob.html',locals(),context_instance=RequestContext(request))