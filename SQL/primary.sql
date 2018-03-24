-----------------主键约束---------------------
唯一性
1.复合主键
CREATE TABLE yangxiao0(
	num char(10) comment 'xuexiao',
	cou char(10) comment '代码',
	sco tinyint unsigned default 60 comment '成绩',
	--复合主键,学号课程一一对应,具有唯一性
	primary key (num, cou);
)charset utf8;

2.追加主键
CREATE TABLE yangxiao1(
	num char(10) comment 'xuexiao',
	cou char(10) comment '代码',
)charset utf8;
--添加主键两种方法
alter table yangxiao1 modify nun char(10) primary key commet 'xuexiao';
alter table yangxiao1 add primary key(num);

--插入数据
insert into yangxiao values('29','234','65'),('27','245','100');
--主键冲突(重复)插入符合键中会冲突
=================索引==============================
定义：系统根据某种算法，将已有的数据(未来可能新增数据),单独建立一个文件，
  	文件能够实现快速的匹配数据，并能够快速的找到对应表中的记录
 索引的意义：
 	1.提升查询数据的效率
 	2.约束数据的有效性（唯一性）
 前提条件：索引本身会产生文件，可能文件很大消耗磁盘空间


