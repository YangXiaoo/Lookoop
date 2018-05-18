# coding: utf-8
from __future__ import division 
import uuid 
import urllib

from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.http import HttpResponse

import paramiko
from ssh.api import *
from ssh.models import *
from ssh.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@defend_attack
def Login(request):
    '''
    登录
    '''
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'GET':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            userinfo = get_object(User, username=username)
            if userinfo is not None:
                if userinfo.is_active == 1:
                    # login(request, user)
                    request.session['role_id'] = 0
                    request.session.set_expiry(3600) # one hour
                    return HttpResponseRedirect(reverse('index'))
                else:
                    error = '用户未激活'
            else:
                error = '用户或密码错误'
        else:
            error = '用户名或密码未正确输入'
    return render_to_response('login.html',{'error':error})


@login_required(login_url='/login')
def Logout(request):
    '''
    注销
    '''
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@require_login
def index(request):
    '''
    主页
    '''
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

@require_login
def asset_list(request):
    '''
    主机列表
    '''
    keyword = request.GET.get('keyword', '')
    export = request.GET.get('export', '')
    asset_find = Asset.objects.all()
    if keyword:
        asset_find = Asset.filter(
            Q(hostname__contains=keyword) |
            Q(ip__contains=keyword) |
            Q(username__contains=keyword) |
            Q(cpu__contains=keyword) |
            Q(memory__contains=keyword) |
            Q(disk__contains=keyword) |
            Q(brand__contains=keyword) |
            Q(system_version__contains=keyword)
            )
    if export:
        pass # excel文件下载
    return render_to_response('asset_list.html', locals(), context_instance=RequestContext(request))

def asset_add(request):
    default_port = 22
    if request.method == 'POST':
        asset_post = AssetForm(request.POST)
        ip = request.POST.get('ip', '')
        hostname = request.POST.get('hostname', '')
        is_active = True if request.POST.get('is_active') == '1' else False
        try:
            if Asset.objects.filter(hostname=unicode(hostname)):
                error = u'主机名 %s 重复(Hostname repeated)' % hostname
                raise ServerError(error)
            if len(hostname) > 54:
                error = u'主机名不能超过53位(the length of hotsname must less than 53)'
                raise ServerError(error)
        except ServerError:
            pass
        else:
            if asset_post.is_valid():
                asset_save = asset_post.save(commit=False)
                password = request.POST.get('password', '')
                password_encode = CRYPTOR.encrypt(password)
                asset_save.password = password_encode
                asset_save.is_active = is_active
                asset_save.save()
                asset_save.save_m2m()
                msg = u'主机 %s 添加成功' % hostname
            else:
                msg = u'主机 %s 添加失败' % hostname
    return render_to_response('asset_add.html', locals(), context_instance=RequestContext(request))

def asset_del(request):
    pass
