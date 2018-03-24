范式
定义：  Normal Format，是一种离散数学中的知识，是为了解决一种数据的存储与优化
		的问题。
		保存数据的存储之后，凡是能够通过关系寻找出来的数据，坚决不再重复。
		终极目标是减少数据的冗余。
范式：	是一种分层结构的规范，分为六层。每一层都比上一层更加严格，要满足于
		下一层必先满足于上一层范式。

六层范式：	1NF,2NF,...
	MYsql属于关系型数据库，有空间浪费，致力于节省存储空间，设计数据库的时候，
	会利用到范式来指导。
	数据库不单要解决空间问题，要保证效率。范式只为了解决空间问题，有指导意义，
	只有前三种范式需要满足。
==========1NF===========
第一范式：在设计表存储数据的时候，如果表中设计的字段存储数据，在取出使用之前
		  还需要额外的处理(拆分)，那么所表的设计不满足第一范式：要求所有字段
		  具有原子性，不可分割。
----------------------------------------------------------------
name   |    class    |  sex  | room   |   代课开始结束时间		|
xx     |    class    |  xx   | xx     |   xx.xx.xx,xx.xx.xxx 	|
-----------------------------------------------------------------
	若查询出来需要直接显示代课开始和结束的时间就需要拆分代课开始
结束的时间。(本身不合理)
	解决方案：将代课时间拆成两个字段
=========2NF===========
第二范式：在数据表设计的过程中，如果有复合主键(多字段主键),并且表中有字段
		  并不是由整个主键来确定，而是依赖主键中的某个字段(主键部分)；存在
		  字段依赖主键的部分的问题，称之为部分依赖：第二范式就是要解决表涉
		  不允许出现依赖部分。
		  name和class共同组成复合主键，代课时间段依赖name和class，但sex不
		  依赖class,room不依赖name，出现了部分依赖，不符合二范式。
解决1：将性别和讲师单独成表，班级与教师单独成表
解决2：取消复合主键，使用逻辑主键ID = 讲师+班级(业务逻辑，复合唯一键)。
       表中添加一列,ID。
=========3NF============
第三范式：	必须满足第二范式。理论上来讲，一张表中所有的字段应该直接依赖
			主键(逻辑主键：代表的是业务主键),如果表涉及中存在一个字段，
			并不直接依赖主键，而是通过某个非主键字段依赖，最终实现依赖主键：
			把这种不是直接依赖主键，而是依赖非主键字段的依赖关系称之为传递依赖。

A给B钱，B又将钱给C，则C的钱来自于A，形成传递依赖。
----------------------------------------------------------------
id 	| 	name   |    class    |  sex  | room   |   代课开始结束时间		|
xx 	|	xx     |    class    |  xx   | xx     |   xx.xx.xx,xx.xx.xxx 	|
-----------------------------------------------------------------
以上设计方案：性别依赖讲师存在，讲师依赖主键；教师依赖班级，班级依赖主键；
			  性别和教师都存在传递依赖。
解决方案： 	将形成传递依赖的字段，以及依赖的字段本身单独取出，形成一个单
			独的表后，然后再需要对应的信息的时候，使用对应的实体表的主键
			加进来。
---------------------------代课表-------------------------------------
id 	| 	name_id   |    class_id    |  代课开始结束时间		|
xx 	|	xx     	  |    class       |    xx.xx.xx,xx.xx.xxx 	|
-----------------------------------------------------------------
------讲师表------
id |  name  | sex |
xx |   xx   | xx  |
-------------------
-----班级表---------
id |  class  | room |
xx |   xx    | xx   |
--------------------
形成逻辑主键。只要能通过其他地方查到的数据就不要直接写入，取消数据的冗余。
=============================逆规范化============================
如果通过关联表获得数据，理论上可以获得，但效率会低一些，会可以在某一些
表中，不去保存另外表的主键(逻辑主键)，而是直接保存想要的数据信息：这样的时候
一张表即可获得数据，而不需要多表查询，但是会导师数据冗余。
    如代课表中姓名和教师直接写入值，而不用逻辑主键。
逆规范化：磁盘利用率与效率的对抗。
范式越多，效率越低。一般大的数据库，磁盘冗余越大，不需要考虑磁盘内存。