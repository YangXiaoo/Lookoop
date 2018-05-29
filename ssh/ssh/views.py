# coding: utf-8
from __future__ import division 
import uuid 
import urllib
from collections import Iterable

from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.db.models import Q

import paramiko
from ssh.api import *
from ssh.models import *
from ssh.forms import *
from ssh.settings import MAIL_ENABLE
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
    request.session['role_id'] = ''
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
        asset_find = Asset.objects.filter(
            Q(hostname__contains=keyword) |
            Q(ip__contains=keyword) |
            Q(username__contains=keyword) |
            Q(cpu__contains=keyword) |
            Q(memory__contains=keyword) |
            Q(disk__contains=keyword) |
            Q(brand__contains=keyword) |
            Q(system_version__contains=keyword)
            )
    if asset_find:
        pass
    else:
        msg = u'没有匹配到'
        asset_find = Asset.objects.all()
    if isinstance(asset_find,Iterable) is False:
        iters = 0

    # excel文件下载
    if export:
        re = write_excel(asset_find)
        if re[0]:
            file_name = re[1]
        msg = u'excel文件已生成，点击下载！'
        return render_to_response('asset_excel_download.html', locals(), context_instance=RequestContext(request)) 
    assets_list, p, assets, page_range, current_page, show_first, show_end = pages(asset_find, request)
    return render_to_response('asset_list.html', locals(), context_instance=RequestContext(request))


@require_login
def asset_add(request):
    '''
    增添主机
    '''
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
                # password_encode = CRYPTOR.encrypt(password)
                password_encode = password
                asset_save.password = password_encode
                asset_save.is_active = is_active
                asset_save.save()
                asset_post.save_m2m()
                msg = u'主机 %s 添加成功' % hostname
            else:
                msg = u'主机 %s 添加失败' % hostname
        return HttpResponseRedirect(reverse('asset_list')) 
    return render_to_response('asset_add.html', locals(), context_instance=RequestContext(request))


@require_login
def asset_edit(request):
    '''
    编辑主机信息
    '''
    asset_id = request.GET.get('id', '')
    asset = get_object(Asset, id=asset_id)
    if asset:
        password_old = asset.password
    af = AssetForm(instance=asset)
    if request.method == 'POST':
        af_post = AssetForm(request.POST, instance=asset)
        ip = request.POST.get('ip', '')
        hostname = request.POST.get('hostname', '')
        password = request.POST.get('password', '')
        is_active = True if request.POST.get('is_active') == '1' else False
        try:
            asset_test = get_object(Asset, hostname=hostname)
            if asset_test and asset_id != unicode(asset_test.id):
                emg = u'该主机名 %s 已存在!' % hostname
                raise ServerError(emg)
            if len(hostname) > 54:
                emg = u'主机名长度不能超过54位!'
                raise ServerError(emg)
            else:
                if af_post.is_valid():
                    af_save = af_post.save(commit=False)
                    if password:
                        af_save.password = password
                    else:
                        af_save.password = password_old
                    af_save.is_active = True if is_active else False
                    af_save.save()
                    af_post.save_m2m()
                    smg = u'主机 %s 修改成功' % ip
                else:
                    emg = u'主机 %s 修改失败' % ip
                    raise ServerError(emg)
        except ServerError as e:
            error = e.message
        return HttpResponseRedirect(reverse('asset_list'))
    return render_to_response('asset_edit.html', locals(),context_instance=RequestContext(request))


@require_login
def asset_del(request):
    '''
    删除主机资料
    '''
    asset_id = request.GET.get('id','')
    if asset_id:
        Asset.objects.filter(id=asset_id).delete()
    if request.method == 'POST':
        asset_batch = request.GET.get('arg', '')
        asset_id_all = str(request.POST.get('asset_id_all', ''))
        if asset_batch:
            for asset_id in asset_id_all.split(','):
                asset = get_object(Asset, id=asset_id)
                asset.delete()
    return HttpResponse(u'删除成功')


@require_login
def web_terminal(request):
    '''
    ssh连接
    '''
    asset_id = request.GET.get('id')
    asset = get_object(Asset, id=asset_id)
    return render_to_response('web_terminal.html', locals())


@require_login
def user_add(request):
    '''
    堡垒机用户添加
    '''
    error = ''
    msg = ''

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = PyCrypt.gen_rand_pass(16)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        uuid_r = uuid.uuid4().get_hex()
        ssh_key_pwd = PyCrypt.gen_rand_pass(16)
        is_active = True if request.POST.get('is_active') == '1' else False
        send_mail_need = False

        try:
            if '' in [username, password, ssh_key_pwd, name]:
                error = u'带*内容不能为空'
                raise ServerError
            check_user_is_exist = UserPar.objects.filter(username=username)
            if check_user_is_exist:
                error = u'注意：用户 %s 重复' % username
                user_de = get_object(UserPar, username=username)
        except ServerError:
            pass
        else:
            try:
                user = db_add_user(username=username, name=name,
                                   password=password,
                                   email=email, uuid=uuid_r,
                                   ssh_key_pwd=ssh_key_pwd,
                                   is_active=is_active,
                                   date_joined=datetime.datetime.now())
                server_add_user(username=username, ssh_key_pwd=ssh_key_pwd)
                user = get_object(UserPar, username=username)
            except IndexError, e:
                error = u'添加用户 %s 失败 %s ' % (username, e)
                try:
                    db_del_user(username)
                    server_del_user(username)
                except Exception:
                    pass
            else:
                user_add_mail(user, password=password, ssh_key_pwd=ssh_key_pwd)
                msg = get_display_msg(user, password=password, ssh_key_pwd=ssh_key_pwd, send_mail_need=send_mail_need)
    return render_to_response('user_add.html', locals(),context_instance=RequestContext(request))


def key_down(request):
    uuid_r = request.GET.get('uuid', '')
    if uuid_r:
        user = get_object(UserPar, uuid=uuid_r)
        if user:
            username = user.username
            private_key_file = os.path.join(KEY_DIR, 'user', username+'.pem')
            print private_key_file
            if os.path.isfile(private_key_file):
                f = open(private_key_file)
                data = f.read()
                f.close()
                response = HttpResponse(data, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(private_key_file)
                return response
    return HttpResponse('No Key File. Contact Admin.')


@require_login
def user_list(request):
    '''
    堡垒机用户列表
    '''
    keyword = request.GET.get('keyword', '')
    export = request.GET.get('export', '')
    user = UserPar.objects.all()
    if keyword:
        user = UserPar.objects.filter(
            Q(name__contains=keyword) |
            Q(password__contains=keyword) |
            Q(username__contains=keyword) |
            Q(ssh_key_pwd__contains=keyword) 
            )
    if user:
        pass
    else:
        msg = u'没有匹配到'
        user = UserPar.objects.all()
    if isinstance(user,Iterable) is False:
        iters = 0
    if export:
        pass # excel文件下载
    return render_to_response('user_list.html', locals(), context_instance=RequestContext(request))


@require_login
def user_del(request):
    '''
    删除ssh登录用户
    '''
    if request.method == "GET":
        user_id = request.GET.get('user_id','')
    elif request.method == "POST":
        user_id = request.POST.get('user_id','')
    else:
        return HttpResponse('Error request')

    user = get_object(UserPar, id=user_id)
    logger.debug(u"删除用户 %s 成功" % user.username)
    ssh_del_user(user.username)
    user.delete()
    return HttpResponse('删除成功')


@require_login
def host_add(request):
    '''
    堡垒机用户主机绑定
    '''
    if request.method == 'GET':
        username = request.GET.get('username', '')
        user = get_object(UserPar, username=username)
        user_id = user.id
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        ip = request.POST.get('ip', '')
        port = request.POST.get('port', '22')
        hostname = request.POST.get('hostname', '')
        asset = get_object(AssetGroup, id=user_id)
        af = AssetGroupForm(instance=asset)
        af_post = AssetGroupForm(request.POST, instance=asset)
        is_active = True if request.POST.get('is_active') == '1' else False
        try:
            if len(hostname) > 54:
                emg = u'主机名长度不能超过54位!'
                raise ServerError(emg)
            else:
                if af_post.is_valid():
                    af_save = af_post.save(commit=False)
                    af_save.is_active = True if is_active else False
                    af_save.port = port
                    af_save.save()
                    af_post.save_m2m()
                    smg = u'主机 %s 添加成功' % ip
                else:
                    emg = u'主机 %s 添加失败' % ip
                    raise ServerError(emg)
        except ServerError as e:
            error = e.message
        return HttpResponseRedirect(reverse('user_list'))
    return render_to_response('host_add.html', locals(),context_instance=RequestContext(request))



@require_login
def host_list(request):
    '''
    资产列表
    '''
    if request.method == "GET":
        user_id = request.GET.get('user_id', '')
        asset = AssetGroup.objects.filter(user_id=user_id)
        user = get_object(UserPar, id=user_id)
        if isinstance(asset,Iterable) is False:
            iters = 0
    else:
        asset = AssetGroup.objects.all()
        if instance(asset,Iterable) is False:
            iters = 0
    return render_to_response('host_list.html', locals(), context_instance=RequestContext(request))


@require_login
def host_edit(request):
    '''
    资产编辑
    '''
    pass


@require_login
def host_del(request):
    '''
    资产删除
    '''
    if request.method == "GET":
        host_id = request.GET.get('id','')
    elif request.method == "POST":
        host_id = request.POST.get('id','')
    else:
        return HttpResponse('Error request')
    host = get_object(AssetGroup, id=host_id)
    logger.debug(u"删除主机 %s 成功" % host.hostname)
    host.delete()
    return HttpResponse('删除成功')


def asset_excel_download(request):
    pass


@require_login
def upload(request):
    if request.method == "GET":
        return render_to_response('upload.html', locals(), context_instance=RequestContext(request))
    else:
        upload_files = request.FILES.getlist('file',None)
        msg = upload_files
        date_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        upload_dir, filename_path = get_tmp_dir()
        ip = get_client_ip(request)
        tmp_file = []
        try:
            for upload_file in upload_files:
                file_path = '%s/%s' % (upload_dir, upload_file.name)
                file_dir = '%s/%s' % (filename_path, upload_file.name)
                size = upload_file.size
                up_file = UpFiles(ip=ip,file_name=upload_file.name,file_path=file_dir, dirs=file_path, size=size)
                up_file.save()
                with open(file_path,'w') as f:
                    for chunk in upload_file.chunks():
                        f.write(chunk)
        except:
            file_path = '%s/%s' % (upload_dir, upload_files.name)
            file_dir = '%s/%s' % (filename_path, upload_files.name)
            size = upload_files.size
            up_file = UpFiles(ip=ip,file_name=upload_files.name,file_path=file_dir, dirs=file_path, size=size)
            up_file.save()
            with open(file_path,'w') as f:
                for chunk in upload_files.chunks():
                    f.write(chunk)
        return render_to_response('upload.html', locals(), context_instance=RequestContext(request))       


@require_login
def download(request):
    '''
    文件下载
    '''
    files = UpFiles.objects.all()
    if request.method == "GET":
        keyword = request.GET.get('keyword', '')
        file_dir = request.GET.get('download', '')
        file_path = os.path.join(BASE_DIR, 'static/files', file_dir)
        if os.path.isfile(file_path):
            f = open(file_path)
            data = f.read()
            f.close()
            response = HttpResponse(data, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
            return response
    elif request.method == "POST":
        file_id = request.POST.get('id', '')
    if keyword:
        files = UpFiles.objects.filter(
            Q(file_name__contains=keyword)  
            )
    if isinstance(files,Iterable) is False:
        iters = 0
    files_list, p, file, page_range, current_page, show_first, show_end = pages(files, request)
    return render_to_response('download.html', locals(), context_instance=RequestContext(request))


@require_login
def file_del(request):
    '''
    文件删除
    '''
    if request.method == "GET":
        file_id = request.GET.get('id','')
    elif request.method == "POST":
        file_id = request.POST.get('id','')
    else:
        return HttpResponse('Error request')
    file = get_object(UpFiles, id=file_id)
    logger.debug(u"删除文件 %s 成功" % file.file_name)
    try:
        file_delete(file)
    except:
        msg = '删除失败'
    file.delete()
    msg = '删除成功'
    return HttpResponse(msg)    

@require_login
def file_edit(request):
    if request.method == "GET":
        file_id = request.GET.get('id','')
        file_name = request.GET.get('name','')
    elif request.method == "POST":
        file_name = request.POST.get('name', '')
        file_id = request.POST.get('id','')
    else:
        return HttpResponse('Error request')
    file = get_object(UpFiles, id=file_id)
    file.file_name = file_name
    try:
        file.save()
        status = 1
        info = 'ok'
    except:
        status = 0
        info = 'fail'
    return HttpResponse(json.dumps({
                "status": status,
                "info": info
            })) 

