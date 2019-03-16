// cpp_notebook.cpp

顺序容器：
	vector
	deque
	list
	forward_list
	array
	string

1. 初始化
	C c;
	C c1(c2);
	C c1 = c2;
	C c{a, b, c, d};
	C c = {a, b, c, d};
	C c(b, e);
	C seq(n);
	C seq(n, t); // n个t

2.容器赋值
	c1 = c2;
	c = {a, b, c, d};
	swap(c1, c2);
	c1.swap(c2);
	// assign不适用于关联容器与array
	seq.assign(b, e);	// b, e区间元素不能指向seq
	seq.assign(c);		// seq区间元素替换为初始化列表c中的元素
	seq.assign(n, t); 	// seq中的元素替换为n个值为t的元素

3. 向顺序容器中添加元素
	// array不支持这些操作
	// forward_list有自己专有版本得insert和emplace
	// forward_list不支持push_back, emplace_back
	// vector和string不支持push_front, emplace_front

	c.push_back(t);			//在c尾部创建值为t或由args创建的元素,返回void。 emplace_
	c.emplace_back(args); 	// back中的args会使用构造函数

	c.push_front(t);
	c.emplace_front(args);

	c.insert(p, t);		// 在迭代器p指向的元素之前创建一个值为t或由args创建的元素。返
	c.emplace(p, args);	// 回指向新添加元素的迭代器

	c.insert(p, n, t);	// 在迭代器p指向的元素之前创建n个值为t的元素。返回指向新添加的
						// 第一个元素的迭代器。若n为0，返回p

	c.insert(p, b, e);	// 同上，插入b和e指定元素，若范围为空，返回p

	c.insert(p, il);	// il是一个花括号包围的元素列表， 将这些元素插入到p指向元素之
						// 返回指向新添加的第一个元素的迭代器。若列表为空，返回p

4. 在顺序容器中访问元素
	// at和下标操作只适用于string, vector, deque, array
	// back不适用于forward_list
	c.back();	// 返回c中尾元素的引用。c为空，函数行为未定义
	c.front();	// 首元素引用。c为空，函数行为未定义
	c[n];		// n为无符号整型,若n>c.size(),函数行为未定义
	c.at(n);	// 若下标越界，则抛出out_of_range

5. 删除元素
	// 删除元素会改变容器大小, 不适用于array
	// forward_list有特殊版本的erase
	// forward_list不支持pop_back
	// vector和string不支持pop_front
	c.pop_back();	// 若为空则函数未定义。函数返回void
	c.pop_front();

	c.erase(p);		// 删除迭代器p指向的元素，返回一个指向被删元素之后元素的迭代器，若
					// p指向尾元素，则返回尾后(off-the-end)迭代器。若p是尾后迭代器，则
					// 函数未定义

	c.erase(b, e);	// 删除迭代器b和e指定范围元素。返回一个指向最后一个被删除元素之后元
					// 素的迭代器。若e为尾迭代器，则函数也返回尾迭代器。

	c.clear();		// 删除c中的所有元素。返回void

6. forward_list中插入或删除元素[p313]

7. 改变容器的大小
	c.shrink_to_fit();	// 只适用于vector, string, deque
	// 下面两种只适用于vector, string
	c.capacity();		// 不重新分配内存空间的话还能保存多少元素。
	c.reserve(n);		// 分配至少能容纳n个元素的空间

8. 构造string的其他办法
	string s(cp, n);	// s是cp指向的数组中前n个字符的拷贝，该数组至少有n个字符

	string s(s2, pos);	// s是string s2从下标pos2开始的字符的拷贝。若pos2>s2.size(),
						// 构造函数的行为未定义

	string s(s2, pos2, len2);	// s是string2从下标pos2开始len2个字符的拷贝

9. string字符串操作
	// args参数见p324
	s.substr(pos, n);	// 返回一个string, 包含s中从pos开始的n个字符的拷贝。pos的默认
						// 值为0。 n的默认值为s.size()-pos,即从pos开始的所有字符。

	s.erase(pos, len);	// 删除从pos开始的len个字符，若len被省略，则删除pos开始到s末尾
						// 的所有字符，返回一个指向s的引用

	s.append(args);		// 将args追加到s。返回一个指向s的引用

	s.replace(range, args);	// 删除range范围内的元素，替换为args指定的元素
							// s.replace(11, 3, "xxx");	// 下标和一个长度
							// s.replace(it_b, it_e, "xxx");	// 一对指向s的迭代器
10. string搜索操作
	s.find(args);	// 第一次出现的位置
	s.rfind(args);	// 最后一次出现的位置
	s.find_first_of(args);	// 查找args中任何一个字符第一次出现的位置
	s.find_last_of(args);	// 查找args中任何一个字符最后一次出现的位置
	s.find_first_not_of(args);	// 在s中查找第一个不存在args中的字符
	s.find_last_not_of(args);	// 在s中查找最后一个不存在args中的字符
	// args必须是以下形式之一
	// c, pos 		从s中位置pos开始查找字符c。pos默认为0
	// s2, pos 	从s中位置pos开始查找字符串s2。pos默认为0
	// cp, pos 	从s中位置pos开始查找指针cp指向的以空字符结尾的C风格字符串。pos默认0
	// cp, pos, n 	从s中位置pos开始查找指针cp指向的数组的前n个字符。pos和n无默认值

11. 容器适配器
	// 库还定义了三种顺序容器是配器：stack, queue, priority_queue
	// 所有容器适配器支持的操作和类型
	size_type
	value_type
	container_type
	关系运算符: ==, !=, <, <=, >=, >
	a.empty();
	a.size();
	swap(a, b);
	a.swap(b);

12. 栈操作
	// 除了11中列出的操作还有以下操作
	// 栈默认基于deque实现，也可以在list或vector之上实现
	s.pop();			// 删除栈顶元素，但不范湖改元素值
	s.push(item);		// 压入栈顶
	s.emplace(args); 	// 压入栈顶
	s.top();			// 返回栈顶元素但不弹出

13. 队列操作
	// 除了11中的操作queue, priority_queue还有以下操作
	// queue默认基于queue实现，priority_queue默认基于vector
	q.pop();
	q.front();	// 返回首元素或尾元素但不删除此元素
	q.back();	// 只适用于queue
	q.top();	// 返回最高优先元素, 但不删除钙元素,只适用于priority_queue
	q.push(item);
	q.emplace(args);
