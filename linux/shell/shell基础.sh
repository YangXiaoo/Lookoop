#date(2018-4-10)
#参考书籍：Linux命令行与shell脚本编程大全(第3版)
[root]# ln -s test.txt test1.txt #硬链接
[root]# sort -M file #排序，常用-nr，详细见P80

shell的父子关系
---------------
1)进程列表-一种命令分组(command grouping)
	()：创建出子shell
	{}：不会创建出子shell

[root]# jobs #显示后台运行的进程
	-l 可以看见更多信息
2)协程
在后台生成一个子shell并在这个子shell中执行命令
[root]# coproc sleep 10 #一般用法
[root]# coproc my_shell { sleep 10; } #设置名称

3)外部命令
衍生(forking),外部执行时，会创建一个子进程。会产生一个全新环境的子进程，使用成本高
[root]# type -a cd #查看一个命令是外键命令还是内建命令
[root]# which cd #只显示外部命令

4)内建命令
	如 cd, exit,
	(1)使用history
		[root]# history #查看历史命令
		[root]# cat .bash_history #查看历史命令，新开终端加载history
		[root]# history -a #写入.bash_history
		[root]# history -n #强制重新加载
	(2)alias


Linux环境变量
-------------
1)全局变量
	[root]# env #查看所有全局变量
	[root]# printenv PATH #获取单个全局变量
	[root]# echo $PATH #引用全局变量
	[root]# ls $PATH #列出全局变量
2)局部变量
	[root]# set #显示局部变量和全局变量

3)自定义变量
	(1)局部变量
		[root]# first_va="one" #在子进程中无效，父进程中也无效
	(2)全局变量
		[root]# second_var="two"
		[root]# export second_var #子进程中有效，但子进程对该值的修改不会影响父进程，删除变量也是
	(3)删除环境变量
		[root]# unset first_va #删除变量

*使用变量用$,操作变量不用$
4)添加环境变量
	[root]# PATH=$PATH:/usr/local/redis/bin #直接添加环境变量
	[root]# vim /etc/profile #第二种方法
	[root]# vim /etc/bashrc #第三种方法，还有其余地方可以修改P115

5)数组变量
	[root]# third_va=(one two three) #设置数组变量
	[root]# echo $third_va #结果为 one
	[root]# echo ${third_va[2]} #结果为three
	[root]# echo ${third_va[*]} #结果为 one two three
	[root]# unset ${third_va[2]} #删除three

Linux文件权限
-------------
1)安全性
	(1)/etc/passwd文件
		该文件下存放用户有关信息
	(2)/etc/shadow文件
		用户密码
	(3)添加新用户
		[root]# useradd -D #查看该命令新增用户的默认值
		GROUP=100 #被添加到GID为100的公共组
		HOME=/home #新用户的目录位于home下
		INACTIVE=-1 #新用户账户密码在过期后不会被禁用
		EXPIRE= #新用户账户未被设置过期日期
		SHELL=/bin/bash #新用户默认将bash shell作为默认的shell
		SKEL=/etc/skel #系统会将/etc/skel目录下的内容复制到新用户目录下
		CREATE_MAIL_SPOOL=yes #在mail目录下创建一个用于接收邮件的文件
	(4)修改用户
		[root]# usermod -l new_name old_name #修改用户名
        参数：
             -c<备注>：修改用户帐号的备注文字；
			 -d<登入目录>：修改用户登入时的目录；
			 -e<有效期限>：修改帐号的有效期限；
			 -f<缓冲天数>：修改在密码过期后多少天即关闭该帐号；
			 -g<群组>：修改用户所属的群组；
			 -G<群组>；修改用户所属的附加群组；
			 -l<帐号名称>：修改用户帐号名称；
			 -L：锁定用户密码，使密码无效；
			 -s<shell>：修改用户登入后所使用的shell；
			 -u<uid>：修改用户ID；
			 -U:解除密码锁定。
		[root]# passwd user #修改用户密码
		[root]# chsh -s /bin/csh user #修改用户默认登录shell

2)Linux组 
	(1)添加组
		[root]# groupadd shared #新添加组
	(1)修改组
		[root]# groupmod -n new_gpname old_gpname #修改组名
		[root]# groupmod -g group 519 #将组group的GID改为519

3)Linux文件权限
	(1)文件属性：
		例：-rwxr-xr-x 1 root root  54 Mar 30 15:56 first.sh
			文件属主权限	rwx
			属组成员权限	r-x 
			其它用户权限 	r-x
			文件类型 权限 后面的1表示链接数 拥有者 拥有组 文件大小 修改时间 文件名称
	(2)文件权限 
			根据八进制得到文件权限。将八进制的权限转换为三个二进制，每个用户可以有三个权限,
		分别为rwx,此时二进制表示为111，八进制表示为7;若权限为r-x，二进制表示为101，八进制表
		示为5.
			创建文件的时候所得到的八进制为666，这个值减去umask的后三位值，即表示
		新创建文件的权限值。
		umask 的值在/etc/profile 中修改
	(3)改变权限
		[root]# chmod u-x file #删除文件file属主权限的执行权限
		[root]# chmod g+w file #增加文件file属组的读入权限
		参数：
			u 属主
			g 属组
			o 其他成员
			a 上述所有
			X 赋予执行权限
			s 运行时重新设置UID或GID
			t 保留文件或目录
	(4)改变所属关系
		[root]# chown yangxiao file #改变文件file的属主权限
		[root]# chown yang.yx file #改变文件file的属主权限和属组权限

