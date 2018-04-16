#date(2018-4-16)
*跳板机：跳板机就是一台服务器，开发或运维人员在维护过程中首先统一登录到这台服务器，然后再登到目标设备进行维护
*堡垒机：在一个特定环境下，为保障网络和数据不受外部和内部用户的入侵和破坏，而运用各种技术手段
实时收集和监控网络环境中每一个组成部分的系统状态，安全事件，网络活动，以便及时报警，处理审计责任

1.用户组/用户组
	添加组方便进行授权，用户是授权和登录主题
2.资产组/资产/IDC
	主机信息简介完整，用户自定义备注登录，支持自动获取主页硬件信息
3.sudo/系统用户/授权规则
	支持sudo授权，系统用户用于登录客户端，授权是将用户、资产和系统用户关联起来
4.在线/登录历史/命令记录/上传下载
	在线实时监控用户操作，统计和录像回放用户操作内容，阻断控制，详细记录上传下载
5.上传/下载
	支持文件上传下载，实现rzsz方式
6.默认设置


安装 
---
# 参考文档：http://docs.jumpserver.org/zh/latest/step_by_step.html
[root]# setenforce 0
[root]# systemctl stop iptables.service
[root]# systemctl stop firewalld.service 

#依赖环境
[root]# yum -y install wget sqlite-devel xz gcc automake zlib-devel openssl-devel epel-release git

[root]# wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
[root]# tar xvf Python-3.6.1.tar.xz  && cd Python-3.6.1
[root]# ./configure && make && make install

[root]# cd /opt #建立 Python 虚拟环境
[root]# python3 -m venv py3 
[root]# source /opt/py3/bin/activate

[root]# cd /opt #下载项目
[root]# git clone https://github.com/jumpserver/jumpserver.git
[root]# cd jumpserver && git checkout master

[root]# cd /opt/jumpserver/requirements #安装依赖 RPM 包
[root]# yum -y install $(cat rpm_requirements.txt)
[root]# pip install -r requirements.txt

[root]# yum -y install redis #安装redis
[root]# service redis start 

[root]# yum -y install mariadb mariadb-devel mariadb-server # centos7下安装的是mariadb
[root]# service mariadb start
[root]# mysql
[root]# create database jumpserver default charset 'utf8';
[root]# grant all on jumpserver.* to 'jumpserver'@'127.0.0.1' identified by 'somepassword';

[root]# cd /opt/jumpserver  #修改 Jumpserver 配置文件
[root]# cp config_example.py config.py
[root]# vi config.py  # 我们计划修改 DevelopmentConfig中的配置，因为默认jumpserver是使用该配置，它继承自Config 
/*
class DevelopmentConfig(Config):
    DEBUG = True
    DB_ENGINE = 'mysql'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = 'jumpserver'
    DB_PASSWORD = 'somepassword'
    DB_NAME = 'jumpserver'
...

config = DevelopmentConfig()  # 确保使用的是刚才设置的配置文件
*/
[root]# cd /opt/jumpserver/utils #生成数据库表结构和初始化数据
[root]# bash make_migrations.sh

[root]# cd /opt/jumpserver #运行 Jumpserver
[root]# python run_server.py all 

