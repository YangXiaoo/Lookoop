django基础.py

[root]#  wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate
[root]# tar -xzvf pip-1.5.4.tar.gz
[root]# cd pip-1.5.4
[root]# python setup.py install
[root]# pip install django #安装
[root]# python -m pip install "django<2" #上条指令不能安装，用这条命令
[root]# python -c "import django;print (django.get_version())" #获得版本检测安装
[root]# django-admin startproject messages
[root]# python manage.py startapp online
[root]# python manage.py runserver #开启服务

├── manage.py
├── messages
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   └── wsgi.py
└── online
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

项目设置在 messages/settings.py 中

[root]# vim online/apps.py 
[root]# vim messages/settings.py #配置添加项目	
	'online.apps.OnlineConfig',  #配置