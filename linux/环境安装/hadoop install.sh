# 2018-6-28
# 安装Hadoop
# 安装教程 https://blog.csdn.net/zjsghww/article/details/54867321

# 1 安装java环境
# 下载，解压http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html
[root]# cd /usr
[root]# mkdir java
[root]# cd java # 利用ssh或FTP将java下载到/usr/java目录下
[root]# cp jdk-10.0.1_linux-x64_bin.tar.gz /usr/lib/java
[root]# cd /usr/lib
[root]# tar zxvf java
[root]# vim ~/.bashrc # jdk-10.0.1是为解压目录
export JAVA_HOME=/usr/lib/jdk-10.0.1 
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
export PATH=${JAVA_HOME}/bin:$PATH  
[root]# source ~/.bashrc
# 配置
[root]# sudo update-alternatives --install /usr/bin/java java /usr/lib/jdk-10.0.1/bin/java 50  
[root]# sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jdk-10.0.1/bin/javac 50  
[root]# sudo update-alternatives --config java  

# 2 安装Hadoop
[root]# cd /usr/src 
[root]# wget http://apache.fayea.com/hadoop/common/current2/hadoop-2.9.1.tar.gz
[root]# tar zxvf hadoop-2.9.1.tar.gz
[root]# cd hadoop-2.9.1/etc/hadoop
[root]# vim hadopp-env.sh
export JAVA_HOME=/usr/lib/jdk-10.0.1
export HADOOP_HOME=/usr/src/hadoop-2.9.1
export PATH=$PATH:/usr/src/hadoop-2.9.1/bin
[root]# source hadoop-env.sh
