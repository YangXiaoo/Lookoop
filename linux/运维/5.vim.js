[root]# rpm -qf `which vim`  #查询版本号q查询，f-file

vim是vi的加强版，明显区别是vim可以语句加亮，vim完全兼容vi
分为：编辑模式，命令模式，字符模式

进入编辑模式：a i o(不分大小写)
说明：
	i 当前字符之前插入
	I 行首插入
	a 当前字符之后插入
	A 行位插入
	o 下一行插入
	O 上一行插入
	x 向后删除一个字符
	X 向前删除一个字符
	u 撤销一步，没按一次撤销一次
	ctrl+r 还原撤销的
	r 替换

	：进入命令模式
	v：进入可视模式
	ctrl+v 进入可视块模式   可以进行块选择
		用法：多行注释 ctrl+v，选择需要注释行，按I插入#，按Esc即可完成多行注释
	V 进入可视行模式
	R 擦除改写进入替换模式

光标定位:
	hjkl
	0和home切换到行首，$和end切换到行尾
	gg定位到文档首行，G定位到末行
	3gg或3G快速定位到第3行
	/string(字符串) 查找关键字 若内容较多，用N n来查找  取消 :noh

对文本编辑：
删除，复制，粘贴，撤销
复制：	y 复制一个字符串
	 	yy 复制一行
		nyy 复制n行
		复制的内容在粘贴板，用p进行粘贴
删除：	dd 以行为单位删除
		ndd 删除n行
粘贴：	p
剪切：	dd

命令行模式：
:w 保存
:w! 强制保存
:q 没有进行任何修改退出
:q! 修改了，不保存，强制退出
:wq 保存退出
:wq! 强制保存退出
:x 保存退出

调用外部文件或命令
假设：要写网卡MAC地址，需要查看，在当前vim编辑文件里照着写
快速调用：命令行输入 
			!ifconfig enth0  #调用系统命令，并展示结果
			r 文件名  #把其他文件内容追加到当前目录下

文本替换：
格式：范围(%所有内容) s 分隔符 旧的内容 分隔符 新的内容
	默认是每一行的第一个符合要求的词 (/g 全部)
	例：替换第一到第三行中出现的w替换成yangxiao，若替换所有则后面加/g
	:1,3 s/w/yangxiao      /g  #加上后替换1-3行所有出现的w
	:4 s/w/xin   #只替换第4行
	:% s/w/xin/gi  #所有w不区分大小写全部替换为xin
---------------------------
ewdewcwe
cwe
cw
wc
w
----
eyangxiaodewcwe
cyangxiaoe
cyangxiao
yangxiaoc
w
-------------------------------
自定义vim使用环境
	临时设置：
	:set nu #设置行号
	:set nonu #取消行号
	永久设置环境：
	[root]# vim /etc/.vimrc  #影响所有用户
	[root]# vim ~/.vimrc  #只能影响当前用户
	set nu
	:wq 保存退出 

vim打开多个文件：
	[root]# vim -o /etc/passwd /etc/hostname   #上下显示
	[root]# vim -O /etc/passwd /etc/hostname   #左右显示，使用ctrl+ww切换编辑

	[root]# vimdiff /etc/passwd test.txt  #比较文件内容

打开乱码解决方案：
	[root]# iconv -f gb2312 -t utf8 test.txt  #test.txt文件乱码解决
文件串行解决：
	[root]# rpm dos2nuix  #centos6需要安装dos2nuix
	[root]# unix2dos test1.txt #解决串行
	[root]# sz test1.txt #发送到windows本地

删除所有文件:
	[root]# rm -rf/*   #删除所有文件，*代表所有         */

Linux文件由三部分组成：
	文件名 test.txt 
	元数据信息 inode 
	真正存放数据 block

查看inode号：
	[root]# stat test.txt  #查看文件状态
	[root]# ls -i test.txt #直接显示inode号
	[root]# ls -l test.txt #显示详细信息
	