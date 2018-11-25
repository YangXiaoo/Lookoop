# 2018-11-25
# django安装出现问题

# 安装最新版本django需要python3.5+
# 安装python3.6，并是python3.6为linux默认python
[root]# mkdir /usr/local/python3.6.5
[root]# cd /usr/local/python3.6.5 
[root]# wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz 
[root]# tar -xzvf Python-3.6.5.tgz
[root]# cd Python-3.6.5 
[root]# yum install make gcc gcc-c++ 
[root]# ./configure -prefix=/usr/local/python3.6.5 
[root]# make && make install
[root]# cp /usr/bin/python /usr/bin/python.bak 
[root]# rm -f /usr/bin/python 
[root]# ln -s /usr/local/python3.6.5/bin/python3.6 /usr/bin/python 
[root]# python -V

# 更新python后yum会出错
[root]# vi /usr/bin/yum 
#!/usr/bin/python2.7
[root]# vi /usr/libexec/urlgrabber-ext-down
#!/usr/bin/python2.7


# 安装django
[root]# pip install Django==2.1.3
# 出现错误需要更新 [root]# python -m pip install --upgrade pip setuptools
# 安装出错后的安装方法 [root]# python -m pip install django

# 安装完若出现提示则添加全局变量： The script django-admin is installed in '/usr/local/python3.6.5/bin' which is not on PATH.
[root]# vi /etc/profile # 添加全局变量
PATH="$PATH:/usr/local/python3.6.5/bin"
[root]# source /etc/profile
[root]# django-admin startproject web # 进入创建code目录创建应用
