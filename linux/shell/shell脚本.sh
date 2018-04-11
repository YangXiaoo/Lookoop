#shell脚本
#date(2018-4-11)
#参考书籍：Linux命令行与shell脚本编程大全(第3版)

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
		[root]# $va1=$[1 + 5]
		[root]# $va2=$[$va1 * 2] #结果为12
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
#detect parameter of input
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
