// js是脚本语言

var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值

document.write("你好 \
世界!");

// 变量名要求
变量必须以字母开头
变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
变量名称对大小写敏感（y 和 Y 是不同的变量）


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

var var1 = 1;	// 不可以配置全局属性，不可以删除
var2 = 2;		// 没有使用var声明，可以配置全局属性，可以删除

// 字符串属性
constructor	返回创建字符串属性的函数
length	返回字符串的长度
prototype	允许您向对象添加属性和方法
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

// 运算符
x = 5+5;	// 10
y = "5"+5;	// 55
z = "Hello" + 5;	// Hello5

// 比较运算符
=== 	绝对等于（值和类型均相等）	
!==	 	不绝对等于（值和类型有一个不相等，或两个都不相等）
// 条件运算符
variablename = (condition)?value1:value2 

// 条件语句
if (condition1)
{
    当条件 1 为 true 时执行的代码
}
else if (condition2)
{
    当条件 2 为 true 时执行的代码
}
else
{
  当条件 1 和 条件 2 都不为 true 时执行的代码
}

// switch
switch(n)
{
    case 1:
        执行代码块 1
        break;
    case 2:
        执行代码块 2
        break;
    default:
        与 case 1 和 case 2 不同时执行的代码
}

// for 语句
var person={fname:"John",lname:"Doe",age:25}; 
for (x in person)  // for/in 语句循环遍历对象的属性
{
    txt = txt + person[x];
}

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

// 调试
console.log(c);	//  调试窗口打印值