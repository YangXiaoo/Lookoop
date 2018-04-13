#shell脚本
#date(2018-4-11)
#参考书籍：Linux命令行与shell脚本编程大全(第3版)

CLI(command-line interface)

基本脚本
--------
1)echo 用法
	-n 将文本字符串与命令输出显示在一行
2)命令替换
	(1)使用 ``
	(2)使用 $()
	实例：
		#!/bin/bash
		date=`date +%y%m%d`
		ls /tmp/test -al > log.$date
	结果：
	-rw-r--r-- 1 root   root   287 4月  11 16:44 log.180411
3)输出重定向
	>  输出重定向
	<  输入重定向，command < inputfile ,将文件内容重定向到命令
	<< 内联重定向(inline input redirection),指定文本标记的开始结尾
4)管道连接(piping)
	输出重定向和输入重定向连用时。
	[root]# rpm -qa | sort #得到软件列表，然后排序
	[root]# rpm -qa | sort | more #使用文本分页命令
	[root]# rpm -qa | sort > list.txt #联合重定向使用

5)数学运算
	(1)expr 
	(2)使用方括号
		[root]# $va1=$[ 1 + 5 ]
		[root]# $va2=$[ $va1 * 2 ] #结果为12
	(3)浮点运算
		使用bc计算器
			[root]# bc -q #进入计算器并不显示欢迎字符
		脚本中使用
			var=$(echo "scale=4; 3.7 / 4" | bc) #scale=4表示显示四位小数
		内联重定向使用bc
			#!bin/bash
			var1=10
			var2=20.23

			var3=$(bc << EOF
			scale = 4
			a1=(var1 * var2)
			a2=(var1 / var2)
			a1 + a2
			EOF
			)
			echo $var3 

6)退出脚本
	(1) $?
		一个脚本运行完毕后会产生一个退出状态码
		0 	命令成功结束
		1 	一般性未知错误
		2 	不适合的shell命令
		126 命令不可执行
		127 没有找到命令
		128 无效的退出参数
		130 通过CTRL+C终止命令
		255 正常范围之外的退出状态码
	(2)自定义退出状态码
		exit 22 #退出状态码
		exit $va3 #可以使用变量
		自定义状态码超过255后会求模计算得到退出状态码

结构化命令
----------

1) if命令
 	if command1 
 	then
 		command set 1 
 	elif command2 
 	then
 		command set 2 
 	fi

2) test 
	(1)test condition #条件成立则返回0状态码，不成立返回其它状态码
		替代test:
		if [ condition ]
		then 
			command
		fi
	(2)数值比较
		if [ $va1 -gt $va2 ]
		比较：
			 -eq,-ge ,-gt ,-le ,-lt ,-ne.不能再test中比较浮点值
	(3)字符串比较
		根据ASC码来比较大于符号要加转义符
		-n 检查字符串长度是否非0，不是0返回状态码0
		-z 检查字符串长度是否为0，若为0返回状态码0
	(4)文件比较
		-d file
		-e file 
		-f file 
		-r file 
		-w file 
		-s file 
		-x file 
		-O file 
		-G file 
		file1 -nt file2
		file1 -ot file2 

3) if高级运算
	使用双括号: (( expression )),P256

4) case命令
	case variable in 
	pattern1 | pattern2)
		command1;;
	pattern3)
		command2;;
	*)
		command3;;

5) for命令
	for var in list 
	do 
		command 
	done
	单引号处理办法：	
		(1)使用转义字符
		(2)使用双引号来定义用到单引号的值
	(1)字段分隔符(internal filed separator)
		空格符、制表符、换行符。通过修改环境变量IFS来识别特定分隔符
		IFS=$'\n' #只能识别换行符
		IFS=$'\n':;" #将换行符冒号、分号、双引号作为分隔符"
	(2)可以使用C语言风格的for循环

6)while命令
	while test command 
	do 
		command 
	done 
7) until命令
	until test command 
	do 
		command 
	done 


用户输入处理
-----------
1)命令形参
	(1)读取参数
		$0为程序名，$1第一个参数...直到第九个参数，第十个参数时使用花括号${10}
		name=$(basename $0) #不会返回脚本的目录，只显示脚本名
		$# 显示脚本所输入的参数，参数统计
		${!#} 显示最后一个输入参数，当没有参数时，显示脚本名
		$* 将所有参数当做单个参数
		$@ 得到所有参数并且可以遍历
		shift 移动变量
	(2)查找选项
		使用 case 
#!/bin/bash
#detect parameters of input
count=1
while [ -n "$1" ]
do
  case "$1" in
  -a) echo "found command a";;
  -b) para="$2"
      echo "found command b and para=$para"
    shift 1;;
  -p)
    $para="$2"
	echo "parameter #$count : $para"
	count=$[ $count + 1 ]
 	shift 1;;
   *) echo "error use command";;
	esac
	shift
done

2)使用getopt(s)命令P300
	(1)getopt optstring parameters
		set -- $(getopt -q ab:cd "$@")
	(2)getopts optstring variable 
		getopts :ab:c opt #opt为参数变量
		说明：自动去除单破折号直接遍历opt即可
		$OPTIND:在getopts处理每个选项时，会将OPTIND环境变量值加1，通过shift可获得之后的参数

3)read命令
	(1)基本读取
		read name #获得输入存入name中
		echo -n #不换行
		read -p "Enter your name:" name #不换行获得输入参数
		若没有指定变量，则会将任何接收到的数据存入REPLY中
	(2)技巧
		#5s未输入参数则返回一个非零退出状态码，只读前10位字符
		read -t 5 -n10 -p "Enter your name：" name
		read -s #隐藏输入内容


呈现数据
#date(2018-4-12)
--------
1)linux文件描述符
	0 STDIN
	1 STDOUT
	2 STDERR
	一共有9个，剩下6个可以自定义
	(1)将错误信息重定向到文件
		[root]# ls -la nosuchdoc 2> log.txt #将读取的错误信息记入log.txt而不是直接显示
		[root]# ls -la file 2> log.txt 1> file.txt 
		[root]# ls -la file &> info.txt #同时写入Info.txt文件中
	(2)永久重定向
		exec 1>testout #将shell脚本的所有标准输出重定向到testout文件中
	(3)定义重定向输出
		exec 3>&1 #描述符3重定向到描述符1
		exec 1>testout #STDOUT的输出重定向到testout文件中
		exec 1>&3 #恢复重定向STDOUT
	(4)定义重定向输入
		exec 6<&0
		exec 0< testin
		exec 0<&6 #恢复标准重定向
	(5)关闭文件描述符
		exec 3>&- #关闭
		关闭之后重新使用所定向的文件会重新创建，原有数据被覆盖
	(6)列出文件描述符  
		lsof -a -p $$ -d 0,1,2 
		#说明：-a 布尔运算，-p 指定进程PID，$$ 当前PID,-d 要显示的文件描述编号
	(7)阻止命令输出
		/dev/null  #空文件，不存储文件，可以清空文件和不输出文件的输入输出定向

2)创建文件
	(1)创建临时文件
		mktemp test.xxxxxx #在/tmp目录下创建唯一名字的文件
		tempfile=$(mktemp test.xxxxxx) #脚本中使用创建的文件名
		tempfile=$(mktemp -t test.xxxxxx) #脚本中使用创建的文件全路径/tmp/test.Aj321
	(2)创建临时目录
		mktemp -d dir.xxxxxx #创建临时目录
3)记录消息
	date | tee -a file #将显示的信息输出到屏幕和指定文件，-a 追加

4)实例：	
	#!/bin/bash
	outfile='mysql.sql'
	IFS=','
	while read uname upasswd uemail uage 
	do 
		cat >> $outfile << EOF
		INSERT INTO studens (uname,upasswd,uemail,uage) VALUES
		('$uname','$upasswd','$uemail','$uage');
		EOF
	done < ${1} 


控制脚本
--------
1)Linux信号
	1-SIGHUP,2-SIGINT,3-SIGQUIT,9-SIGKILL,15-SIGTEAM,17-SIGSTOP,18-SIGTSTP,19-SIGCONT
	(1)生成信号
		CTRL+C SIGINT 
		CTRL+Z SIGTSTP 
	(2)捕获信号
		trap commands signals
		trap "echo 'i have trapped ctrl+c'" SIGINT #捕获Ctrl+c组合，显示语句，并阻止程序停止命令
		trap "echo 'goodbye...'" EXIT #退出时输出goodbye
		trap -- SIGINT #删除捕获信号
		trap -SIGINT #恢复默认行为
2)非控制台下运行脚本
	nohup 命令   让脚本一直以后台模式运行到结束

3)作业控制
	启动、停止、终止以及恢复作业的这些功能统称为作业控制。
	jobs 查看作业
	参数：
		-l 列出进程PID及作业号
		-n 只列出上次shell发出的通知后改变了状态的作业
		-p 只列出作业的PID
		-r 只列出运行中的作业
		-s 只列出已停止的作业
	jobs命令输出结果中 
	 	未指定任何作业号表示该作业会被当做控制命令的操作对象
	 -	当前默认作业处理完后，带减号的作业会成为下一个默认作业
	 + 	被当做默认作业
	 bg 后台模式重启
	 fg 前台模式重启

4)运行优先级
	好人难做！
	nice -n -10 test.sh  #以优先值为-10来运行该脚本
	renice -n 10 -p 333 #调整PID为333的进程以优先值10来运行


函数
----
菜单脚本
#!/bin/bash
#this is a menu
#执行字符串前面的数字即可选择指令
function diskplace {
	clear 
	df -k
}

function whouse {
	clear
	who
}

function memuse {
	clear
	free
}

PS3="enter option: "
select option in "disk" "whouse" "memuse" "exit"
do
	case $option in
	"disk")diskplace;;
	"whouse")whouse;;
	"memuse")memuse;;
	"exit")break;;
	*)clear;echo "wrong selection";;
	esac
done
clear
--------)

使用dialog窗口的升级版菜单
安装dialog
[root]# yum install -y dialog #yum安装后直接使用
-------------------------
#!/bin/bash
#update of menu-v-1.0
tmp1=$(mktemp -t test.xxxxxx) #在/tmp中生成文件
tmp2=$(mktemp -t test2.xxxxxx)

function hostname {
	hostname > $tmp1
	dialog --textbox $tmp1 20 60
}

function user {
	who > $tmp1
	dialog --textbox $tmp1 20 60
}

function memery_info {
	free > $tmp1
	dialog --textbox $tmp1 20 60
}
function ifconfig {
	ifconfig > $tmp1
	dialog --textbox $tmp1 20 60
}

while [ 1 ] #无限循环
do
	dialog --menu "Simple Menu" 20 30 10 1 "Hostname" 
	2 "user" 3 "memery info" 4 "ifconfig" 0 "Exit" 2> $tmp2
	if [ $? -eq 1 ]  # $? 上个命令的退出状态，出现错误则退出
	then 
		break
	fi 

	selection=$(cat $tmp2)
	case $selection in 
	1)
		hostname;;
	2)
		user;;
	3)
		memery_info;;
	4)
		ifconfig;;
	0)
		break;;
	*)
		dialog --msgbox "Sorry, invalid selection..." 10 30
	esac
done
rm -f $tmp1 2> /dev/null #空文件不记录数据，重定向STDOUT
rm -f $tmp2 2> /dev/null 