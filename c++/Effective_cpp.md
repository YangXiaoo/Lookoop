
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