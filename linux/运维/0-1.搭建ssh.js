#date(2018-4-7)

1.清空iptables
[root]# iptables -F
[root]# vim /etc/selinux/config #SELINUX=disabled 
[root]# reboot #重启
[root]# getenforce #查看
