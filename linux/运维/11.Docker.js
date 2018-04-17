#date(2018-4-16)

工作流程:服务器A运行docker Engine 服务，在docker Engine上启动很多容器container，从
外网Docker Hub 上把image操作系统镜像下载下来，放到container容器运行。这样虚拟机实例就可以运行下来。
最后通过Docker client 对dockerrong虚拟化平台进行控制。

Image可以理解为系统镜像，虚拟机关机状态的磁盘文件；Container是Image在运行时的一个状态，虚拟磁盘
文件，包括内存数据。

Docker核心技术
	1.Namespace -实现Container的进程，网络，消息，文件系统和主机名的隔离
	2.Cgroup -实现对资源的配额和度量
[root@yangxiao ~]# vim /etc/yum.repos.d/docker.repo
[root@yangxiao ~]# chmod +x !$
chmod +x /etc/yum.repos.d/docker.repo
[root@yangxiao ~]# cat  /etc/yum.repos.d/docker.repo
[dockerrepo]
name=Docker Repository
baseurl=http://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgacheck=0
[root@yangxiao ~]# echo 1 > /proc/sys/net/ipv4/ip_forward
[root@yangxiao ~]# systemctl start docker 
[root@yangxiao ~]# vim /etc/yum.conf #keepcache=1保存安装文件
[root@yangxiao ~]# service docker start

#另一种方法
# yum install https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm  
# 
[root@yangxiao ~]# docker search centos #搜索符合的镜像文件

#从Docker hub 下载一个镜像
[root@yangxiao ~]# docker pull centos 
[root@yangxiao ~]# docker load -i centos-latest-docker-image.tar #方法二
[root@yangxiao ~]# du  -sh /var/lib/docker #文件目录

使用 
----
运行一个container并加载镜像centos，运行这个实例之后，在实例中执行/bin/bash命令
[root@yangxiao ~]# docker run -i -t centos /bin/bash 
-i 以交互模式运行容器，通常与-t同时使用
-t 为容器重新分配一个伪输入端，通常与-i同时使用
[root@yangxiao ~]# exit #退出

在container中长久运行一个进程
-----------------------------
[root@yangxiao ~]# JOB=$(docker run -d centos /bin/sh -c "while true;do echo hello world;sleep 1;done")
-d 后台运行，并返回容器ID
-c 待完成
[root@yangxiao ~]# echo $JOB #容器的ID号

从容器中取日志
[root@yangxiao ~]# docker logs $JOB 
[root@yangxiao ~]# docker ps -a #列出所有运行中的容器
[root@yangxiao ~]# docker kill $JOB #杀死容器
[root@yangxiao ~]# docker restart ID #ID 为进程号，start,stop
[root@yangxiao ~]# docker rm -f ID #移除容器进程

Docker Image 制作方法
------------
1)docker image
docker commit <container id> <image_name>
#创建一个新的容器，并安装好nmap工具
[root@yangxiao ~]# yum install nmap-ncat -y
[root@yangxiao ~]# exit
[root@yangxiao ~]# docker commit 34dde33c2ah3  centos:nmap 
[root@yangxiao ~]# docker run -t -i centos:nmap /bin/bash #启动新创建的docker

2)docker build 
[root@yangxiao ~]# mkdir /docker-build
[root@yangxiao ~]# cd !$
[root@yangxiao ~]# touch Dockerfile #make自动化编译时需要Makefile文件，自动化创建docker镜像时，需要Dockerfile
[root@yangxiao ~]# vim Dockerfile 
FROM centos  #基于centos镜像
MAINTAINER userabc <1270009836@qq.com> #MAINTAINER镜像创建者
RUN yum -y install httpd   #RUN安装软件使用
ADD start.sh /usr/local/bin/start.sh #ADD将文件放到container的文件系统对应的路径
ADD index.html /var/www/html/index.html 
[root@yangxiao ~]# vim start.sh 
[root@yangxiao ~]# echo "usr/sbin/http-DFOREGROUND" >start.sh  #类似于systemctl start httpd
[root@yangxiao ~]# chmod a+x start.sh 
[root@yangxiao ~]# echo "docker image build test" > index.html

#语法 docker build -t 父镜像：自己定义的镜像名 Dockerfile路径
-t 表示tag，用于指定新的镜像名

Docker Image 的发布
--------------
1)save image to tarball
#docker save -o xxx.tar 本地镜像名

2)发布到Docker Hub 




实战
使用生成的centos:httpd 镜像，启动容器，然后将容器中的80端口映射到docker物理机上的9000端口上
[root@yangxiao ~]# docker run -d -p 9000:80 centos:httpd /bin/sh -c /usr/local/bin/start.sh

#查看一个正在运行的container
[root@yangxiao ~]# docker exec -ti ID /bin/bash #ID-想要查看的容器ID