/*
第n个斐波那契数, 第0个为0
*/
// 2019-12-2

function Fibonacci(n)
{
    var a = 0, b = 1, c = 0, it = 1;
    while (it < n) {
        c = a + b;
        a = b;
        b = c;
        it++;
    }
    
    return c;
}

function test() {
	var n = 0;
	var ret = Fibonacci(n);
	console.log(ret);
}

test()