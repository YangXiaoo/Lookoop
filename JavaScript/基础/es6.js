// 变量的解构赋值

// 数组的解构赋值, 只要某种数据结构具有Iteration接口，都可以采用数组形式解析
var [a, b, c] = [1,2,3]	// 同样适用于let, const
// console.log(a)

// 对象的解构赋值
var { foo, bar } = { foo: 'a', bar: 'b' }
// console.log(foo)

// 字符串的解构赋值
const [ac, bc, cc, dc, ec] = 'hello'
let {length: len } = 'hello'	// 对数组对象的length属性解构赋值
// console.log(len)

// 数值和布尔值的解构赋值
let {toString: s} = 123
if (s === Number.prototype.toString) {
	// console.log('true')
}

// 函数参数的解构赋值
function move({x = 0, y = 0} = {}) {
	return [x, y]
}

// console.log(move({x: 3}))	// [ 3, 0 ]

// 解构赋值用途
// 1. 交换变量的值
// console.log(a, b);
[a, b] = [b, a]
// console.log(a, b)

// 2. 从函数返回多个对象
var foo = () => {
	return {
		foo: 1,
		bar: 2
	};
}
var { foo1, bar1 } = foo()

// 3. 函数参数的定义
// 4. 提取JSON数据
// 5. 参数的默认值
var foo2 = (url, {p1=true, p2=3}) => {}

// 6. 遍历Map结构
var map = new Map()
map.set('first', 'hello')
map.set('second', 'second')

for (let [k, v] of map) {
	// console.log(k + ' is ' + v);
}
for (let [k] of map) {
	// 获得key
}
for (let [, v] of map) {
	// 获得value
}

// 7. 输入模块的指定方法

//-----------------------------------------------

// 字符串

//-----------------------------------------------
// 函数扩展
// 使用默认值
var foo3 = (x, y = 'defaultValue') => {}

// rest参数
function add(...values) {
	let sum = 0
	for (var val of values) {
		sum += val
	}

	return sum
}

add(2,3,4)

// rest其余用法
const sortNumbers = (...numbers) => numbers.sort();

// ...(扩展运算符), 将数组转为用逗号分隔的参数序列, 只要具有Iteration接口对象都可以使用扩展运算符

console.log(...[1,2,3])	// 1,2,3

// 替代数组的apply方法

// 不需要apply将数组转换为函数的参数
function f(x, y, z) {
// ...
} 
// f(...args);

// Math用法
Math.max(...[2,1,4])

// 数组push用法
// arr1.push(...arr2)

// 字符串转换为数组
// [...'hello']	// ['h', 'e', 'l', 'l', 'o']

// Map
// [...map.keys()]

// es6允许使用=>定义函数
// 箭头函数有几个使用注意点。
// （1） 函数体内的 this 对象， 就是定义时所在的对象， 而不是使用时所在的对象。
// （2） 不可以当作构造函数， 也就是说， 不可以使用 new 命令， 否则会抛出一个错误。
// （3） 不可以使用 arguments 对象， 该对象在函数体内不存在。 如果要用， 可以用Rest参数代替。
// （4） 不可以使用 yield 命令， 因此箭头函数不能用作Generator函数。

// 嵌套的箭头函数
function insert(value) {
	return {into: function (array) {
			return {after: function (afterValue) {
			array.splice(array.indexOf(afterValue) + 1, 0, value);
			return array;
		}};
	}};
}

// 变为
let insert2 = (value) => ({into: (array) => ({after: (afterValue) => {
array.splice(array.indexOf(afterValue) + 1, 0, value);
return array;
}})});

// 函数绑定
// ::, 左边是一个对象，右边是一个函数，自动将左边对象作为上下文环境(this对象)，绑定到右边的函数上面
// obj::func;
// 等同于
// bar.bind(foo)

// foo::bar(...arguments);
// // 等同于
// bar.apply(foo, arguments);

// 尾调用优化


// ------------------------------------
// 对象的扩展
// 属性的简洁表示
var foo = 'bar';
var baz = {foo};	// 等同于 var baz = {foo: bar};
// baz // {foo: "bar"}

var o = {
	method() {
		return "Hello!";
	}
};
// 等同于
var o1 = {
	method: function() {
		return "Hello!";
	}
};

// 使用Object.is()比较两个值是否严格相等

// Object.assign(obj1, obj2, obje)	// 将obj2,obj3中的对象和Obj1结合，属于浅拷贝


// ------------------------------------
// Proxy和Reflect, 在目标对象之前架设一层拦截，可以对外界的访问进行过滤和改写
var obj2 = new Proxy({}, {
	get: function (target, key, receiver) {
		console.log(`getting ${key}!`);
		return Reflect.get(target, key, receiver);
	},
	set: function (target, key, value, receiver) {
		console.log(`setting ${key}!`);
		return Reflect.set(target, key, value, receiver);
	}
});

// ------------------------------------
// Set和Map
var set = new Set()
set.add(1)		// return Set本身
set.size
set.delete(1)	// return boolean
set.has(1)
set.clear()

// keys() ： 返回一个键名的遍历器
// values() ： 返回一个键值的遍历器
// entries() ： 返回一个键值对的遍历器
// forEach() ： 使用回调函数遍历每个成员

// 实现并集，交集，差集
let a3 = new Set([1, 2, 3]);
let b3 = new Set([4, 3, 2]);
// 并集
let union = new Set([...a3, ...b3]);
// [1, 2, 3, 4]
// 交集
let intersect = new Set([...a3].filter(x => b3.has(x)));
// [2, 3]
// 差集
let difference = new Set([...a3].filter(x => !b3.has(x)));

// forEach遍历操作
a3.forEach((value, key) => console.log(value * 2) )


// Map
// 键必须为字符串
// 方法
Map.set(key, value)
Map.size
Map.get(key)
Map.has(key)
Map.delete(key)
Map.clear()

// Map原生提供三个遍历器生成函数和一个遍历方法。
keys()： 返回键名的遍历器。
values()： 返回键值的遍历器。
entries()： 返回所有成员的遍历器。
forEach()： 遍历Map的所有成员。

// Map转换为数组
[...map]

// Map的其它转换见pdf-P221

// ------------------------------------
// Generator函数
// 是一个普通函数，但是有两个特征：1.function关键字与函数名之间有一个*号；2.函数内部使用yield语句 
function* helloWorldGenerator() {
	yield 'hello';
	yield 'world';
	return 'ending';
} 
var hw = helloWorldGenerator();
hw.next()
hw.next()

// ------------------------------------
// Class
// 调用原型上的方法
class Point {
	constructor(x, y) {
		this.x = x
		this.y = y
	}

	toString() {
		return ''
	}

	// 只有静态方法没有静态属性
	static classMethod() {
		return 'hello'
	}
}

// 继承
class colorPoint extends Point {
	constructor(x, y, color) {
		super(x, y)
		this.color = color
	}

	toString() {
		return super.toString()
	}
}

// class有两条继承连：prototype, __proto__(指向对一个构造函数的prototype属性)