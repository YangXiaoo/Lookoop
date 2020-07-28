// js是脚本语言

var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值

// 变量名要求
// 变量必须以字母开头
// 变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
// 变量名称对大小写敏感（y 和 Y 是不同的变量）


var carname = "Volvo"; 
var carname;	// 值仍然为"Volvo"
var cars = new Array();	// 数组
cars[0] = "Saab";
cars[1] = "Volvo";
cars[2] = "BMW";

var person = {firstname:"John", lastname:"Doe", id:5566};	// 对象
name = person.lastname;
name = person["lastname"];

cars=null;	// 清空变量值
person=null;

// 声明变量类型
var carname=new String; // 返回的是一个对象
var x =     new Number;
var y =     new Boolean;
var cars =  new Array;
var person = new Object;

// 变量作用域
- 变量在函数内部没有声明属于全局变量，声明后属于局部变量
- 函数外部属于全局变量
- 函数参数只在函数内起作用，是局部变量
// let与var的区别
let : 局部变量
var : 如果不使用var则为全局变量如下
var2 = 1;   // 全局变量


var var1 = 1;	// 不可以配置全局属性，不可以删除
var2 = 2;		// 没有使用var声明，可以配置全局属性，可以删除

// 字符串属性
constructor	返回创建字符串属性的函数
length	返回字符串的长度
prototype	允许您向对象添加属性和方法

// function属性
arguments // 属于数组类，函数不用写形参即可直接访问arguments属性读取参数
fn.length // 函数参数个数

// 原型属性和实例属性
    方法                  适用范围            描述
for..in 数组，               对象        获取可枚举的实例和原型属性名
Object.keys()               数组，对象   返回可枚举的实例属性名组成的数组
Object.getPropertyNames()   数组，对象   返回除原型属性以外的所有属性（包括不可枚举的属性）名组成的数组
Object.getOwnPropertyNames()方法返回一个由指定对象的所有自身属性的属性名（包括不可枚举属性但不包括Symbol值作为名称的属性）组成的数组
for..of 可迭代对象(Array, Map, Set, arguments等)  返回属性值

    
// ----------------------------------------------------------
// 字符串函数
charAt()	返回指定索引位置的字符
charCodeAt()	返回指定索引位置字符的 Unicode 值
concat()	连接两个或多个字符串，返回连接后的字符串
fromCharCode()	将 Unicode 转换为字符串
indexOf()	返回字符串中检索指定字符第一次出现的位置
lastIndexOf()	返回字符串中检索指定字符最后一次出现的位置
localeCompare()	用本地特定的顺序来比较两个字符串
match()	找到一个或多个正则表达式的匹配
replace()	替换与正则表达式匹配的子串
search()	检索与正则表达式相匹配的值
slice()	提取字符串的片断，并在新的字符串中返回被提取的部分
split()	把字符串分割为子字符串数组
substr()	从起始索引号提取字符串中指定数目的字符
substring()	提取字符串中两个指定的索引号之间的字符
toLocaleLowerCase()	根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射
toLocaleUpperCase()	根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射
toLowerCase()	把字符串转换为小写
toString()	返回字符串对象值
toUpperCase()	把字符串转换为大写
trim()	移除字符串首尾空白
valueOf()	返回某个字符串对象的原始值

// es6
var s = 'hello'
s.includes('el', 开始搜索的位置-可选)
s.startWith('hello', 开始搜索的位置-可选)
s.endsWith('o', 开始搜索的位置-可选)
// 使用模板字符串, {}内可以进行运算以及引用对象属性，调用函数
console.log(`this is ${var}`)

// -------------------------------------------------------------------------
// 数组函数
// https://blog.csdn.net/qq_39132756/article/details/85007082
length 数组长度
concat()    连接两个或更多的数组，并返回结果。 可以用于复制新的数组 newArr = arr1.concat();
join()  把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。
pop()   删除并返回数组的最后一个元素
splice(index,howmany) 删除指定位置元素
push()  向数组的末尾添加一个或更多元素，并返回新的长度。
reverse()   颠倒数组中元素的顺序。
shift() 删除并返回数组的第一个元素
unshift()：方法可向数组的开头添加一个或更多元素，并返回新的长度
slice(start , end) 从某个已有的数组返回选定的元素, end可选
sort()  对数组的元素进行排序
splice()    删除元素，并向数组添加新元素。
toSource()  返回该对象的源代码。
toString()  把数组转换为字符串，并返回结果。
toLocaleString()    把数组转换为本地数组，并返回结果。
valueOf()   返回数组对象的原始值
indexOf(item,start) （从数组的开头（位置 0）开始向后查找）tem： 必须。查找的元素。start：可选的整数参数。规定在数组中开始检索的位置。如省略该参数，则将从array[0]开始检索。
lastIndexOf(item,start) （从数组的末尾开始向前查找）item： 必须。查找的元素。start：可选的整数参数。规定在数组中开始检索的位置。如省略该参数，则将从 array[array.length-1]开始检索。

array.forEach(function(currentValue , index , arr){//do something}, thisValue)
    currentValue : 必需。当前元素
    index： 可选。当前元素的索引值。
    arr :  可选。当前元素所属的数组对象。
    thisValue： 可选。传递给函数的值一般用 "this" 值。如果这个参数为空， "undefined" 会传递给 "this" 值

array.map(function(currentValue , index , arr){//do something}, thisValue)  ， 指映射，方法返回一个新的数组
array.filter(function(currentValue , index , arr){//do something}, thisValue) 过滤”功能，方法创建一个新数组, 其包含通过所提供函数实现的测试的所有元素
array.every(function(currentValue , index , arr){//do something}, thisValue) 判断数组中每一项都是否满足条件，只有所有项都满足条件，才会返回true。
array.some(function(currentValue , index , arr){//do something}, thisValue) 判断数组中是否存在满足条件的项，只要有一项满足条件，就会返回true。
归并方法：reduce()、reduceRight()
Array.from() 方法是用于类似数组的对象（即有length属性的对象）和可遍历对象转为真正的数组。
    let json ={
        '0':'卢',
        '1':'本',
        '2':'伟',
        length:3
    }
    let arr = Array.from(json);
    console.log(arr); // ["卢", "本", "伟"]

Array.of() 方法是将一组值转变为数组，参数不分类型，只分数量，数量为0返回空数组
Array.of(1,2,3,4, undefined) // [1,2,3,4, undefined]
Array.fill()方法用一个固定值填充一个数组中从起始索引到终止索引内的全部元素。不包括终止索引。 语法：array.fill(value,  start,  end)
var arr = new Array(3).fill(7)  // [7,7,7]

Array.find(value, index, arr)
[1, 5, 10, 15].find(function(value, index, arr) {
    return value > 9;
}) // 10

Array.includes(searchElement ,  fromIndex) 方法用来判断一个数组是否包含一个指定的值，如果是返回 true，否则false。
    searchElement ： 必须。需要查找的元素值。
    fromIndex：可选。从该索引处开始查找 searchElement。如果为负值，则按升序从 array.length + fromIndex 的索引开始搜索。默认为 0。

遍历数组方法 keys()、values()、entries()
这三个方法都是返回一个遍历器对象，可用for...of循环遍历，唯一区别：keys()是对键名的遍历、values()对键值的遍历、entries()是对键值对的遍历。


// 运算符
x = 5+5;	// 10
y = "5"+5;	// 55
z = "Hello" + 5;	// Hello5

// 比较运算符
=== 	绝对等于（值和类型均相等）	
!==	 	不绝对等于（值和类型有一个不相等，或两个都不相等）
// 条件运算符
variablename = (condition)?value1:value2 



// for 语句
var person={fname:"John",lname:"Doe",age:25}; 
for (x in person)  // for/in 语句循环遍历对象的属性,通常不用于遍历数组
{
    txt = txt + person[x];
}

// 不可以用于对象
for( let i of arr){
    console.log(i);
}

for(let index in array) {  
    console.log(index,array[index]);  
};

// typeof
typeof "John"                // 返回 string 
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true

// JS数据类型
// 5 种不同的数据类型：
string
number
boolean
object
function
// 3 种对象类型：
Object
Date
Array
// 2 个不包含任何值的数据类型：
null
undefined

typeof "John"                 // 返回 string 
typeof 3.14                   // 返回 number
typeof NaN                    // 返回 number
typeof false                  // 返回 boolean
typeof [1,2,3,4]              // 返回 object
typeof {name:'John', age:34}  // 返回 object
typeof new Date()             // 返回 object
typeof function () {}         // 返回 function
typeof myCar                  // 返回 undefined (如果 myCar 没有声明)
typeof null                   // 返回 object

// 判断遍历是否为数组
alert(arr instanceof Array); // true 
alert(arr.constructor === Array); // true 
Array.isArray(arr);

// 调试
console.log(c);	//  调试窗口打印值
console.log(`index: ${index}`)  // 模板打印

// 字符串与数字转换
parseInt(string, type)  // type指定格式转换
Number(string)
num.toString(2) // 将数字转换为二进制形式
toFixed()       // 方法可把 Number 四舍五入为指定小数位数的数字。

// 调用函数有3种方式：
obj.func();
func.call(obj, args);       // obj为对象，在函数中可以调用对象中的属性
                            // args: 参数列出, 必须有多少参数列出多少参数
func.apply(obj, [m,n......]);    // 参数为数组
func.bind(obj)();    // bind返回为目标函数并不调用所以需要()