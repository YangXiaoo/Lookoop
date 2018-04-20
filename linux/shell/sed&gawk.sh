#date(2018-4-12~4-14)
sed(stream editor)
对数据流中的文本执行程序脚本
--------------------
sed [option] '[sed command]' [filename]
-n ：只打印模式匹配的行
-e ：直接在命令行模式上进行sed动作编辑，此为默认选项,使用多个命令用;隔开
-f ：将sed的动作写在一个文件内，用–f filename 执行filename内的sed动作
-r ：支持扩展表达式
-i ：直接修改文件内容

command：
p 	打印匹配行（和-n选项一起合用）
= 	显示文件行号
a\ 	在定位行号后附加新文本信息
		[root]# sed '3a\ Under the third line' data.txt #第三行后插入
i\ 	在定位行号后插入新文本信息
		[root]# sed '3i\ Beyond the third line.' data.txt #第三行前插入新的一行
d 	删除定位行
		#根据数字寻址
		[root]# sed '2,$d' data.txt #删除第二行到末尾的数据
		#文本寻址
		[root]# sed '/1/,/3/d' data.txt #删除匹配到的文本区间，第一个开始，第二个结束，没有匹配到结束符则删除开始之后的所有数据
c\	用新文本替换定位文本，修改行
		[root]# sed '2,3c\ Hello world!' data.txt #替换第二行到第三行
w 	filename 写文本到一个文件，类似输出重定向 >
		[root]# sed '1,2w test.txt' data.txt #将date中的第一二行打印到test中,数据流写入文本
r 	filename 从另一个文件中读文本，类似输入重定向 <
		[root]# sed '3r date.txt' test.txt #将文本内容读入date中，类似于插入date的第三行后面
s 	使用替换模式替换相应模式
		[root]# sed 's/name/yangxiao/w test.txt' data.txt #把date.txt中name替换并重定向到test.txt中
		[root]# sed 's!/bin/bash!bin/bach!' /tec/passwd #用!替换/分隔符
q  	第一个模式匹配完成后退出或立即退出
l 	显示与八进制ACSII代码等价的控制符
{} 	在定位行执行的命令组，用分号隔开
n 	从另一个文件中读文本下一行，并从下一条命令而不是第一条命令开始对其的处理
N 	在数据流中添加下一行以创建用于处理的多行组
g 	将模式2粘贴到/pattern n/
y 	传送字符，替换单个字符
		[root]# sed 'y/abc/def/' data.txt #将abc分别替换为def


1)使用地址
	(1)数字寻址
		[root]# sed '2,$s/name/bob/gi' data.txt #不区分大小写替换第二行到末行
	(2)文本模式过滤器
		[root]# sed '/user/s/name/bob/gi' data.txt #匹配user所在行并替换
2)多行命令
	(1)next命令
		n:让sed编辑器移动到文本的下一行
		N：将下一文本添加到模式空间中已有的文本后
		[root]# sed '/head/{n ; d}' data.txt #匹配head所在行并移至下一行进行删除指令
		[root]# sed 'N ; s/my.name/Youth/' data.txt #若my name不在一行，则可以通过N连接两行，并进行替换。
		[root]# sed 'N ; s/my\nname/D' data.txt #删除my name的第一行,下面为结果
		my 				name
		name    ====>  	is 
		is 				youth
		youth
3)保持空间
	h 模式空间复制到保持空间
	H 模式空间附加到保持空间
	g 将保持空间复制到模式空间
	G 将保持空间附加到模式空间
	x 交换模式空间和保持空间的内容
	[root]# sed -n '{1!G ; h ; $p }' data.txt #反转行，-n阻止脚本输出

4) &符号
	用来代表替换命令中的匹配模式
	[root]# echo "hello world!" | sed 's/[a-z]+ld!$/"&"/g' # hello "world"
5)单独替代  \1第一个子模式
	[root]# echo "this furry cat is pretty" | sed 's/furry\(.at\)/\1/' # this cat is pretty
	[root]# echo "1234567" | sed 's/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/' # 1,234,567
	#1234,567->1,234,567
6)行
	[root]# sed '=' data.txt | sed 'N; s/\n/ /' #文件编号
	[root]# sed '/^$/d ; $!G' data.txt #删除多余的行，并加倍行距,G将保持空间内容附加到模式空间，保持空间只有一个空行。
	[root]# sed '{
	> :start 
	> $q ; N ; 11,$D
	> b start
	> }' data.txt  #列出内容的最后十行
	[root]# sed '/./,/^$/!d' data.txt #删除多余的空白行，只留一个空白行
	[root]# sed '/./,$!d' data.txt #删除开头的空白行
	[root]# sed '{
	> :start
	> /\n*$/{$d; N; b start }
	> }' data.txt #删除结尾的空白行
	[root]# sed 's/<[^>]*>//g ; /^$/d' data.txt #删除HTML标签


gawk
----
gawk options program file  

1)选项
	-F fs 			划分数据字段的字段分隔符
	-f file 		指定的文件中读取程序
	-v var=value	定义一个变量及其默认值
	-mf N 			要处理数据文件中的最大字段数
	-mr N 			数据文件中的最大数据行数
	-W keyword		指定gawk的兼容模式或警告等级
2)数据字段变量
	$0 代表整个文本
	$1 文本中第一个数据字段
	$n 文本中第n个数据字段
3)使用
 	[root]# awk '{print $1}' test2.txt #显示第一列
	[root]# awk -F: '{print $1}' /tmp/test/test2.txt #显示第一列内容
	打印一个头一个尾
	[root]# awk 'BEGIN
	< {print "name level result\n"} 
	< {print $1,$2,$3} 
	< END
	< {print  "end of class1 results"}' .test2.txt
4)使用变量
	(1)数据字段和记录变量
		FS 	输入字段分隔符
		RS 	输入记录分隔符
		OFS 输出字段分隔符
		ORS 输出记录分隔符
		FIELDWIDTHS 由空格分隔的一段数字，定义了每个数据字段宽度
		[root]# gawk 'BEFIN{FS=",";OFS="--"} {print $1,$2,$3}' data.txt
	(2)数据变量
ARGC	 	The number of command line parameters present
ARGIND 		The index in ARGV of the current fle being processed
ARGV 		An array of command line parameters
CONVFMT 	The conversion format for numbers (see the printf statement), with a default value of %.6 g
ENVIRON 	An associative array of the current shell environment variables and their values
ERRNO 		The system error if an error occurs when reading or closing input fles
FILENAME 	The flename of the data fle used for input to the gawk program
FNR 		The current record number in the data fle
IGNORECASE 	If set to a non-zero value, ignores the case of characters in strings used in the gawk command
NF 			The total number of data felds in the data fle
NR 			The number of input records processed
OFMT 		The output format for displaying numbers, with a default of %.6 g
RLENGTH 	The length of the substring matched in the match function
RSTART 		The start index of the substring matched in the match function		
)
5)数组
	for var in array #var为array的索引
	delete array[var] #删除数组变量

6)使用模式 
	[root]# gawk -F: '$1 ~ /rich/{print $1,$NR}' /etc/passwd #匹配rich字段
7)实例：统计每组成绩的总分和平均分
	[root]# cat data.txt 
	bob,team1,20,34,34
	ben,team2,32,12,34
	dol,team2,12,25,34
	ted,team1,32,14,21
	[root]# vim score.sh
	#!/bin/bash
	for team in $(gawk -F, '{print $2}' data.txt | uniq)
	do 	
		gawk -v team=$team 'BEGIN{FS=",";total=0}
		{
			if ($2==team)
				{
					total += $3 + $4 + $5;
				}
		}
		END {  #此处花括号不能换行
			avg=total/6;
			print "Total for",team,"is",total,",the average is",avg
		}' data.txt
	done









正则表达式
----------
1)基本类型
	(1)锚字符
		^ 行首，$行位
	(2)字符组
		[cf] 通过一部分即可匹配，需要匹配特定长度需要锚字符
	(3)排除型字符
		[^cf] #过滤掉cf
	(4)区间
		[0-9],[a-z]
	(5)星号*
		/ik*b/ #匹配k0次或多次
	(6).字符
		/.ed/ #用来匹配处换行符外任意的单个字符(换行符也算字符)
	(7)问号 ?
		匹配0次或一次
	(8)加号
		加号前面的字符可以出现一次或多次，但必须至少出现1次
	(9)使用花括号
		{m} 精确出现m次
		{m,n} 最少m次最多n次
	(10)管道符号
		| 正则表达式和管道符号之间不允许有空格，用逻辑或来指定正则表达式引擎需要的两个或多个模式
	(11)分组
		/m(ab)?/ #匹配m或mab
2)实战：
	(1)验证电话号码 
		(123)456-7890
		(123 6 ) 456-7890
		123-456-7890
		123.456.7890
		^\(?[1-9][0-9]{2}\)?(| |-|\.)[0-9]{3}(|-|\.)[0-9]{4}$
	(2)验证邮箱 username@hostname 
	^([a-zA-Z0-9_\-\.\+]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
	|       username     |@|        域名      |.|   顶级域名   |



