#date(2018-4-9	)
1).list赋值是共享索引，浅拷贝，copy模块
2).字典存储的值经过哈希运算，不可以切片
	创建方式：
	1.大括号包裹键值对:mydict={1:'a',2:'b'}
	2.工厂法创建：mydict=dict(([1,'a'],[2,'b']))
	3.字典内建法：mydict=dict.fromkeys([1,2,3,4,5],'a'),不能独立分配
		清空字典mydict.clear()