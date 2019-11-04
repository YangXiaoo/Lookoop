// 移除数组中与item相等的元素，直接在arr中修改
function removeWithoutCopy(arr, item) {
    var index = 0;
    var arrLength = arr.length;
    for (let it of arr) {
        if (item != it) {
            arr[index++] = it;
        }
    }
    // console.log(`index: ${index}`)
    for (var i = 0; i < arrLength - index; ++i) {
        arr.pop();
    }
    
    return arr;
}

// ---------------------------------------------------------------------------
// 统计数组 arr 中值等于 item 的元素出现的次数
function count(arr, item) {
    var dupCount = 0;
    arr.forEach((val, index) => {
        val === item ? dupCount++ : 0;
    });
    
    return dupCount;
}

// ---------------------------------------------------------------------------
// 找出数组 arr 中重复出现过的元素
function duplicates(arr) {
    var map = {};
    var ret = [];
    
    for (let item of arr) {
        if (item in map) {
            map[item]++;
        } else {
            map[item] = 1;
        }
    }

    for (var key in map) {
        if (map[key] !== 1) {
            ret.push(key);
        }
    }
    return ret;
}

function testDuplicates(arr) {
    return duplicates(arr);
}

// ---------------------------------------------------------------------------
// 为数组 arr 中的每个元素求二次方。不要直接修改数组 arr，结果返回新的数组
function square(arr) {
    return arr.map((val) => {
        return val * val;
    });
}

// ---------------------------------------------------------------------------
// 在数组 arr 中，查找值与 item 相等的元素出现的所有位置
function findAllOccurrences(arr, target) {
    var ret = [];
    arr.forEach((val, index) => {
        if (val === target) {
            ret.push(index);
        }
    });

    return ret;
}

// solution2
function findAllOccurrences2(arr, target) {
    var result=[];
    arr.filter(function(item,index) {
        return item===target&&result.push(index);
    });

    return result;
}

function testFindAllOccurrences(arr, target) {
    return findAllOccurrences(arr, target);
}

// ---------------------------------------------------------------------------
// 存在全局变量修改
function globals() {
    myObject = {
        name : 'Jory'
    };

    return myObject;
}

function globals() {
    let myObject = {    // var也可以
        name : 'Jory'
    };

    return myObject;
}


// ---------------------------------------------------------------------------
// 请修复给定的 js 代码中，函数定义存在的问题
function functions(flag) {
    if (flag) {
        function getValue() { return 'a'; }
    } else {
        function getValue() { return 'b'; }
    }

    return getValue();
}

// 函数声明与函数表达式的区别，函数声明会被解析器在代码执行前解析，所以用的永远是最
// 新的那个即else代码块的声明。改用为函数表达式即可
function functions(flag) {
    var getValue = null;
    if (flag) {
        getValue =  function() { return 'a'; }
    } else {
        getValue = function() { return 'b'; }
    }

    return getValue();
}
// ---------------------------------------------------------------------------
function count(start, end) {
    console.log(start);
    var timer = setInterval(() => {
        if (start < end)
        console.log(++start);
    }, 100);

    return {
        cancle : () => {
            clearInterval(timer);
        }
    };
}

function testCount() {
    var counter = count(0, 10);
}
// ---------------------------------------------------------------------------
// 实现 fizzBuzz 函数，参数 num 与返回值的关系如下：
// 1、如果 num 能同时被 3 和 5 整除，返回字符串 fizzbuzz
// 2、如果 num 能被 3 整除，返回字符串 fizz
// 3、如果 num 能被 5 整除，返回字符串 buzz
// 4、如果参数为空或者不是 Number 类型，返回 false
// 5、其余情况，返回参数 num
function fizzBuzz(num) {
    if (num === null || (typeof num) !== 'number') {
        return false;
    } else if (num % 3 === 0 && num % 5 === 0) {
        return 'fizzbuzz';
    } else if (num % 3 === 0) {
        return 'fizz';
    } else if (num % 5 === 0) {
        return 'buzz';
    } else {
        return num;
    }
}

function testFizzBuzz() {
    console.log(fizzBuzz(3));
    console.log(fizzBuzz(5));
    console.log(fizzBuzz(15));
    console.log(fizzBuzz(2));
    console.log(fizzBuzz('45'));
}
// ---------------------------------------------------------------------------
// 将数组 arr 中的元素作为调用函数 fn 的参数

// 调用函数有3种方式：
// obj.func();
// func.call(obj, args);    // 参数列出, 必须有多少参数列出多少参数
// func.apply(obj, [m,n......]);    // 参数数组
function argsAsArray(fn, arr) {
    return fn.apply(this, arr);
}
// ---------------------------------------------------------------------------
// 将函数 fn 的执行上下文改为 obj 对象
// fn: function () {return this.greeting + ', ' + this.name + '!!!';} 
// obj: {greeting: 'Hello', name: 'Rebecca'}
//apply
function speak(fn, obj) {
    return fn.apply(obj);
}
//call
function speak(fn, obj) {
    return fn.call(obj);
}
//bind
function speak(fn, obj) {
    return fn.bind(obj)();
}

// ---------------------------------------------------------------------------
// 实现函数 functionFunction，调用之后满足如下条件：
// 1、返回值为一个函数 f
// 2、调用返回的函数 f，返回值为按照调用顺序的参数拼接，拼接字符为英文逗号加一个空格，即 ', '
// 3、所有函数的参数数量为 1，且均为 String 类型
function functionFunction1(str) {
    var func = function(arg) {
        return str + ', ' + arg;
    }
    
    return func;
}

function functionFunction(str) {
    var args = Array.prototype.slice.call(arguments);   // 将参数变为数组
    var func = function(str) {
        var tmpArgs =  Array.prototype.slice.call(arguments);

        return functionFunction.apply(null, args.concat(tmpArgs));
    }
    
    func.toString = () => {
        return args.join(', ');
    }

    return func;
}


function testFunctionFunction() {
    console.log(functionFunction('Hello')('world').toString());
}
// ---------------------------------------------------------------------------
// 实现函数 makeClosures，调用之后满足如下条件：
// 1、返回一个函数数组 result，长度与 arr 相同
// 2、运行 result 中第 i 个函数，即 result[i]()，结果与 fn(arr[i]) 相同
// https://www.nowcoder.com/questionTerminal/578026cd24e3446bbf27fe565473dc26?f=discussion
function makeClosures(arr, fn) {
    // 闭包函数
    var ret = [];
    arr.forEach((val) => {
        var f = () => {
            return fn(val);
        };

        ret.push(f);
    });
    
    return ret;
}

function testMakeClosures() {
    var arr = [1, 2, 3];
    var fn = function(x) { return x * x; };

    console.log(makeClosures(arr, fn)[1]());
}
// ---------------------------------------------------------------------------
var arr = [1, 2, 2, 3, 4, 2, 2];
var item = 2;


// console.log(testCount());
testMakeClosures()
