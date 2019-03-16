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


