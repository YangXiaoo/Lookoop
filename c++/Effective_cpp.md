
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
- identity test,不具备异常安全性
- 手工排序语句，先记住原先的指针，然后将原先指针指向新指针，删除原先指针。
- 使用copy-and-swap

## 12. 复制对象时勿忘其每一个成分
- 若copy构造函数与copy assignment操作符有相似代码，消除重复代码做法是建立一个新的成员函数给两者调用。这样的成员函数往往是private，并且常被命名为init。

