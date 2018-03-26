#date(2018-3-26)
#数据备份与还原
数据库备份还原方式：数据表备份，单表备份，SQL备份，增量备份
==========数据表备份
1.不需要通过SQL来备份：直接进入数据库文件夹复制对应的表结构及数据文件
	数据表备份前提条件：不同存储引擎有区别
	存储引擎：mySQL进行数据存储的方式主要两种，innoDb,MyIsAm
查看mysql版本： select @@version
InnoDb:只有表结构，数据全部存储到ibdata中
myisam：结构文件frm，索引文件myi，数据文件myd
文件备份使用与myisam引擎，直接复制三个文件就可以了

myisam 迁移优势好，备份占空间

==========单表数据备份
每次只能备份一张表，只能备份数据(表结构不能备份)，将表中的数据导出到文件

备份：从表中选出一部份数据保存到外部的文件中(outfile)
select *  into outfile 文件路径  files 字段处理 from 数据源 ;#外部文件不存在
--备份整个班的数据表
select * into outfile 'd:/htdocs/mysql/backup/class.txt' from class;
--备份的text不要用txt记事本打开，不然会改变文档编码
--数据间用tab间隔开
set names utf8;#设置编码
=高级备份-针对单表处理
指定字段和行的处理方式
files：字段处理
	enclosed by ：字段用什么包裹，默认控字符串
	terminated by:字段以什么结束，默认"\t"，tab键
	escape by：特殊符号，用什么方式处理，默认"\\"，使用反斜杠转义
	lines:行处理
		starting by:每行开始，默认字符串
		terminated by :每行结束方式
--高级备份
select * into outfile '/htdocs/mysql/backup/class1.txt' 
--字段处理
files 
enclosed by '"'--数据使用双引号包裹
terminated by '|'--数据使用|结尾
lines 
starting by 'START:'
from class;

==========数据还原 
将一个在外部保存的数据重新恢复到表中(如果结构表不存在，不能恢复)
load data infile 文件路径 into table 表名[(字段列表)] files 字段处理 lines 行处理;
--怎么备份，怎么还原
--还原数据
load data infile '/htdocs/mysql/backup/class1.txt'
into table class 
files 
enclosed by '"'--数据使用双引号包裹
terminated by '|'--数据使用|结尾
lines 
starting by 'START:';
==========SQL备份 (针对表结构)
备份：SQL语句，系统对表与结构进行处理编程SQL语句，然后进行备份
还原：执行SQL指令即可还原

备份：mysql没有提供备份指令，使用mysql提供的软件：mysqldump.exe 
mysqldump/mysqldump.exe -hPup 数据库名字 [数据表名1 [数据表名2]] > 外部文件目录(建议sql)
--先退出mysql环境
mysql -q
--进入 系统环境
mysqldump -uroot -proot mydatabase class > /htdocs/mysql/backup/class.sql 
--整库备份
mysqldunp -uroot -proot mydatabase  > /htdocs/mysql/backup/mydatabase.sql
==========SQL还原 
两种方式：
1.使用mysql.exe客户端还原
	mysql.exe/mysql -hPup 数据库名字 < 备份目录
--还原数据
mysql -uroot -proot mydatabase < /htdocs/mysql/backup/mydatabase.sql
2.使用SQL指令
	source 指定文件路径
--SQL还原,现在已经在mydatabase数据库中，以下不用指定路径
source /htdocs/mysql/backup/mydatabase.sql;

SQL优缺点：
1.优点，可以备份结构
2.缺点，浪费空间。额外的增加SQL指令(我认为可以忽略)

==========增量备份-大项目用增量备份
不是针对数据或SQL指令进行备份，对mysql服务器的日志备份
增量备份：指定时间段进行备份，备份数据不会重复，不会浪费空间，所有的操作都会备份
