
## 2. 尽量以const， enumeration， inline替换#define
\#define看到的是指向宏命令的值而不是变量，难以查找错误信息所在位置
- 对于单纯量，最好以const对象或enum替换#define
- 对于形式函数的宏(macros), 最好改用inline替换#define

## 3. 尽可能使用const
- logical constness 与 bitwise-constness

```cpp
class Text {
 public:
	const char& operator[](std::size_t position) const {
		...
		return text[position];
	}
	char& operator[](std::size_t position) {
		return const_cast<char&>(static_cast<const Text>(*this)[position]);
	}
}
```

## 4. 确定对象被使用前已先被初始化
- 对于大多数类型而言，比起先调用default构造函数然后再调用copy assignment操作符，效率更高。
- 如果成员是const或references，必须要初始值不能赋值。
- 构造函数最好使用成员初值列(member initialization list), 而不要使用assignment。初值列列出的成员变量，其排序次序应该和他们在class中的声明次序相同。
- 为免除`跨编译单元之初始化次序`问提，用local static对象替换non-loacl static 对象

```cpp
class FileSystem { ... };
FileSystem &tfs() {
	static FileSystem fs;	// 初始化local static 对象
	return fs;
}
class Directory { ... };
Directory::Directory(params) {
	...
	std::size_t = disks = tfs.num_disks();
}
Directory& tmp_dir() {
	static Directory td;
	return td;
}
Dirctory tmp_dir(); 		// 创建一个tmp_dir不会受tfs是已经先被初始化
```
## 5. 了解C++默默编写并调用哪些函数
编译器可以暗自为class创建default构造函数，copy构造函数，copy assignment操作符，以及析构函数。

## 6. 若不想使用编译器自动生成的函数，就该明确拒绝
- c++11使用=delete。
- 将相应的成员函数声明为private并且不予实现。或者写一个基类将基类的构造或析构函数作为private成员。

## 7. 为多态基类声明virtual析构函数
- 带有多态性质的基类若没有虚析构，删除指向基类的指针对象可能不会释放掉派生类资源
- 若多态性质class拥有任何virtual，它必须拥有一个virtual析构函数
- 若class不是作为基类或不具备多态性质(ploymorphically)，就不该声明virtual析构函数。

## 8. 别让异常逃离析构函数
- 析构函数不要抛出异常。
```cpp
class DBConn {
 public:
	void close() {			// 提供用户使用新函数
		db.close();
		closed = true;
	}
	~DBConn() {
		if (!closed) {
			try {
				db.close();
			}
			catch(...) {
				...			// 捕捉错误并吞下
			}
		}
	}
 private:
 DBConnection db;
 bool closed;
}
```

## 9. 绝不在构造和析构工程中调用virtual函数
- 不会下降至派生类

## 10. 令operator=返回一个reference to *this
- 为实现`连锁赋值`，赋值操作符必须返回一个reference指向操作符左侧的实参。

## 11. 在operator=中处理"自我赋值"
因为在赋值过程中可能自己赋值给自己，可能会造成指针指向null
见p54
三种解决办法：

- identity test,不具备异常安全性。
- 手工排序语句，先记住原先的指针，然后将原先指针指向新指针，删除原先指针。
- 使用copy-and-swap

## 12. 复制对象时勿忘其每一个成分
- 若copy构造函数与copy assignment操作符有相似代码，消除重复代码做法是建立一个新的成员函数给两者调用。这样的成员函数往往是private，并且常被命名为init。

## 13. 以对象管理资源
- 为防止资源泄露，使用RAII对象，它们在构造函数中获得资源并在析构函数中释放资源。
- 两个经常使用的RAII对象分别为shared_ptr,auto_ptr。前者通常是较佳选择，因为其copy行为比较直观。而后者，复制动作会使它指向null。

## 14. 在资源管理类中小心copy行为
- 禁止复制，对底层资源使用引用计数法。
- 复制底部资源，转移底部资源的拥有权。

## 15.在资源管理类中提供对原始资源的访问
- APIs往往要求访问原始资源，所以每个RAII class应该提供一个“取得其所管理资源”的办法。
- 对原始资源的访问可能经由显式转换或隐式转换。一般而言显式转换比较安全，但隐式转换对客户比较方便。

## 16. 成对使用new和delete时要采取相同形式
- 如果在new中使用[]，必须在相应的delete表达式中也是用[]。反之new不使用[],则delete一定不要使用[]。

## 17. 以独立语句将new对象放入智能指针
- 以独立语句将New对象放入只能指针内。如果不这样做，一旦异常被抛出，有可能难以察觉的资源泄露。

```cpp
process(std::shared_ptr<Widget>(new Widget), priority()); // 可能会发生资源泄露
// 上述语句更改
std::shared_ptr<Widget> pw(new Widget);		// 以独立语句存放new对象
process(pw, priority());
```
## 18.让接口容易被使用，不易被误用
- 促进正确使用的办法包括接口一致性，以及内置类型的行为兼容。
- 阻止误用的办法包括建立新类，限制类型上的操作，束缚对象值，以及消除客户的资源管理责任。
- std::shared_ptr支持定制型删除器(custom deleter)。

## 19.设计class犹如设计type
- Treat class design as type design.

## 20. 宁以pass-by-reference-to-const替换pass-by-value
- 比较高效，并且可避免分割问题。
- 不适用内置类型，以及STL的迭代器和函数对象。

## 21. 返回对象时，不要返回其reference
- 返回reference用static，但有时也会有问题。[p93]
- 返回non-static的reference离开局部后其引用指向对象会被销毁。

## 22. 将成员变量声明为private
- 赋予客户访问数据的一致性，可细微划分访问控制，允许约束条件获得保证，并提供class作者以充分的实现弹性。
- protected并不比public更具有封装性。

## 23. 宁以non-member,non-friend替换member函数
- 增加封装性，包裹弹性(packaging flexibility)和机能扩充性。

## 24. 若所有参数皆需要类型转换，请采用non-member函数、
- 如果要为某个函数的所有函数(包括this所指向的那个隐喻参数)进行类型转换，那么这个函数必须是个non-member。

## 25. 考虑写一个不抛出异常的swap函数
- pimpl(pointer to implementation): 以指针指一个对象，内含真正数据的类型

## 26. 尽可能延后变量定义式出现的时间
- 可能未使用就抛出异常
- 考虑变量定义在循环外还是循环内，如下，除非（1）知道赋值成本比"构造+析构"成本低（2）正在处理代码中效率高度敏感的部分，否则应该使用B。

```cpp
// 方法A： 一个构造 + 一个析构 + n个赋值
Widget w;
for (int i = 0; i < n; ++i) {
	w = f(i);
}

// 方法B：n个构造 + n个析构
for (int i = 0; i < n; ++i) {
	Widget w(f(i));
}
```

## 27. 尽量少做转型动作
- const-cast, dynamic_cast, reinterpret_cast, static_cast
- 避免在注重效率的代码中使用dynamic_cast。
- 如果转型是必须，将它隐藏在某个函数背后。客户随后可以调用该函数，而不需要自己使用转型。
- 宁可使用c++-style转型，也不使用旧式转型。

## 28. 避免返回handles指向对象内部成分
- 避免返回handles（包括references，指针，迭代器）指向对象内部成分。

## 29. 为异常安全而努力是值得的
```cpp
// 设计为struct是因为数据的封装性由于`pmimpl被声明为private`而获得保证
struct PMImpl {
	std::shared_ptr<Image> bg_image;
	int image_changes;
}

class Menu {
	...
 private:
 	Mutex mutex;
 	std::shared_ptr<PMImpl> pimpl;
};

void Menu::change_background(std::string &imgsrc) {
	using std::swap;
	Lock ml(&mutex);
	std::shared_ptr<PMImpl> pNew(new PMImpl(*pimpl));
	pNew->bg_image.reset(new Image(imgsrc));	// 修改副本
	++pNew->image_changes;

	swap(pimpl, pNew);	// 置换数据释放mutex
}

```

## 30. 彻底了解inlining的里里外外
- 可能产生代码膨胀问题
- 不要只因为function template出现在头文件就声明为inline。

## 31. 将文件的编译依存关系降至最低
- 相依于声明式，不要相依于定义式。
- 程序库头应该以“完全且仅有声明式(full and declaration-only forms)”的形式存在。

## 32. 确定你的public继承塑模出is-a关系
make sure public inheritance modles "is-a"
- public继承意味is-a。适用于base身上的每一件事情一定适用于derived classes身上，因为每一个derived class对象也都是一个base class对象。

## 33. 避免遮掩继承而来的名称
- 名称遮掩规则对不同参数相同名称的函数适用。
- 为了让遮蔽的名称再见天日，。可以使用using声明或转交函数(forwarding functions)。

## 34. 区分接口继承和实现继承
- pure virtual：只具体制定接口继承。必须重新定义。
- impure virtual: 制定接口继承及缺省实现继承。可以不用重新定义，这样继承缺省版本。
- non-virtual:指定接口函数以及强制性实现继承。不需要重新定义。

## 35. 考虑virtual函数以外的其他选择
- function的行为像一般函数指针。

## 36. 绝不重新定义继承而来的non-virtual函数
- Never redefine an inherited non-virtual function


## 37. 绝不重新定义继承而来的缺省参数值
- 缺省参数值都是静态绑定，而virtual函数-唯一应该覆写的东西-却是动态绑定。

## 38. 通过复合塑模出has-a或根据某事物实现出
- Model "has-a" or "is-implemented-in-terms-of" through composition

## 39. 明智审慎地使用private继承
- EBO(empty base optimization)，一般只在单一继承下使用

## 40.