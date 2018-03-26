#date(2018-3-26)
#函数
代码执行结构有三种：顺序结构，分支结构，循环结构
================================顺序结构==========
实现准备多个代码块，按照条件选择执行某段代码
==========================if分支======================
在mysql中，只有if分支
基本用法：
------------
if 判断条件 then 
	--满足条件要执行的代码
esle 
	--不满足条件执行的代码
end if;
----------
触发器结合if分支：判断商品库存是否足够，不够不能生成订单
--触发器：订单生成之前要判断商品是否满足
delimiter %%
create trigger befor_order before insert on my_order for each row 
begin 
	--获取商品库存
	select inv from my_goods where id = new.g_id into @inv;
	--比较库存：触发器没有提供一个能够阻止时间发生的能力(暴力报错)
	if @inv < new.g_number then 
	--库存不够
		insert into xxx values(xxx);--没有该表，直接报错
	end if;
end
%%

--改回
delimiter ;

---插入订单
insert into  my_order vaues(null,1,1000);




	create trigger befor_order before insert on my_order for each row 
begin 

	select inv from my_goods where id = new.g_id into @inv;

	if @inv < new.g_number then 
		insert into xxx values(xxx);
	end if;
end
%%
=========================循环：while循环==================================
用法：
while 条件判断 do 
	--满足条件要执行的代码
	--变更循环条件
end while;
循环控制：循环内部进行循环的判断和控制
mysql没有对应的continue 和 break但有
iterate迭代，类似continue后面代码不执行，循环重新来过
leave：离开，类似break这个循环结束

使用方式：iterate/leave 循环名字

--定义循环名字：
while 条件 do
	--循环体
	--循环控制
	leave/iterate 循环名字；
end while;

