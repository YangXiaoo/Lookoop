# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
import time
import datetime

ASSET_STATUS = (
    (1, u"已使用"),
    (2, u"未使用"),
    (3, u"报废")
    )
class User(AbstractUser):
    name = models.CharField(max_length = 100)
    uuid = models.CharField(max_length = 100)
    # ssh_passwd = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.username


class Asset(models.Model):
    ip = models.CharField(max_length = 32, blank=True, null=True, verbose_name=u"主机ip")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
    username = models.CharField(max_length = 100, verbose_name=u"登录名")
    password = models.CharField(max_length = 100, verbose_name=u"登录密码")
    hostname = models.CharField(max_length = 100, verbose_name=u"主机名")
    ssh_key = models.CharField(max_length = 100, blank=True, null=True, verbose_name=u"密匙")
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"主机状态")
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    date_add = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")
    comment = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注")
    
    mac = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"MAC地址")
    brand = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'硬件厂商型号')
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    system_arch = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"系统平台")

    def __unicode__(self):
        return self.ip,slef.hostname


class Log(models.Model):
    user = models.CharField(max_length=20, null=True)
    host = models.CharField(max_length=200, null=True)
    remote_ip = models.CharField(max_length=100)
    login_type = models.CharField(max_length=100)
    logfile_path = models.CharField(max_length=100, verbose_name=u"日志路径")
    start_time = models.DateTimeField(null=True)
    pid = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    end_time = models.DateTimeField(null=True)
    filename = models.CharField(max_length=40)

    def __unicode__(self):
        return self.log_path


class UserPar(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    ssh_key_pwd = models.CharField(max_length = 100)
    uuid = models.CharField(max_length = 100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.name


class AssetGroup(models.Model):
    user_id = models.IntegerField(blank=True, null=True, verbose_name=u"关联用户id")
    ip = models.CharField(max_length = 32, blank=True, null=True, verbose_name=u"主机ip")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
    username = models.CharField(max_length = 100, verbose_name=u"登录名")
    password = models.CharField(max_length = 100, verbose_name=u"登录密码")
    hostname = models.CharField(max_length = 100, verbose_name=u"主机名")
    ssh_key = models.CharField(max_length = 100, blank=True, null=True, verbose_name=u"密匙")
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"主机状态")
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    date_add = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")
    comment = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.username


class UpFiles(models.Model):
    ip = models.CharField(max_length=32, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=False, null=False)
    date_add = models.DateTimeField(auto_now=True, null=True)
    file_path = models.CharField(max_length=200)
    dirs = models.CharField(max_length=500)
    size = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.file_name