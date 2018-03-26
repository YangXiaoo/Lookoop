#date(2018-3-26)
#函数
代码执行结构有三种：顺序结构，分支结构，循环结构
===========顺序结构==========
实现准备多个代码块，按照条件选择执行某段代码
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