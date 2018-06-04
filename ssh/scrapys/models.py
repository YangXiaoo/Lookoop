# coding: utf-8
from django.db import models
import time
import datetime

class Job(models.Model):
    title = models.CharField(max_length = 100, null=True)
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    company_link = models.CharField(max_length = 200,null=True)
    work_type = models.CharField(max_length = 20, null=True)
    info_link = models.CharField(max_length = 200,null=True)
    city = models.CharField(max_length = 20, null=True)
    address = models.CharField(max_length = 50)
    lng = models.CharField(max_length = 30, null=True)
    lat = models.CharField(max_length = 30, null=True)
    avg_salary = models.CharField(max_length = 20,null=True)
    educational = models.CharField(max_length = 20,null=True)
    high_salary = models.CharField(max_length = 20,null=True)
    low_salary = models.CharField(max_length = 20,null=True)
    high_exp = models.CharField(max_length = 20)
    low_exp= models.CharField(max_length = 20)
    publish_time = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.name,self.company,self.city,self.educational,self.title


class Handle(models.Model):
    title = models.CharField(max_length = 100, null=True)
    #company = models.CharField(max_length = 100) 
    city = models.CharField(max_length = 20, null=True)
    avg_salary = models.CharField(max_length = 20, null=True)
    iter_count = models.CharField(max_length = 20, null=True)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.title,self.city 

class Edu(models.Model):
    title = models.CharField(max_length = 100, null=True)
    educational = models.CharField(max_length = 20, null=True)
    total_salary = models.CharField(max_length = 20, null=True)
    iter_count = models.CharField(max_length = 20, null=True)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.title,self.educational 


class TopCity(models.Model):
    title = models.CharField(max_length = 100, null=True)
    city = models.CharField(max_length = 20, null=True)
    avg_salary = models.CharField(max_length = 20, null=True)
    # avg_salary is not average of salary, because it did not divided by iter_count
    iter_count = models.CharField(max_length = 20, null=True)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.title,self.city


class WorkType(models.Model):
    title = models.CharField(max_length = 100, null=True)
    work_type = models.CharField(max_length = 20, null=True)
    total_salary = models.CharField(max_length = 20, null=True)
    iter_count = models.CharField(max_length = 20, null=True)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.title,self.work_type


class WorkExp(models.Model):
    title = models.CharField(max_length = 100, null=True)
    exp = models.CharField(max_length = 20, null=True)
    total_salary = models.CharField(max_length = 20, null=True)
    iter_count = models.CharField(max_length = 20, null=True)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.exp,self.title


class AnsysFile(models.Model):
    title = models.CharField(max_length = 100, null=True)
    data_txt = models.CharField(max_length = 100, null=True)
    data_analy = models.CharField(max_length = 100, null=True)
    data_tran = models.CharField(max_length = 100, null=True)
    data_final = models.CharField(max_length = 100, null=True)
    search_count = models.CharField(max_length = 20, null=True,default=0)
    date = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    def __unicode__(self):
        return self.title