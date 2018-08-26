// 2018-7-29 ~ 
// C语法



// 字符串
#include <ctype.h> 
#include <string.h>
char s = "sdss";
isspace(s); // 判断是否为空格或制表符

// 字符串长度
char str[20]="0123456789"; 
int a = strlen(str); // a = 10; 
int b = sizeof(str); // b = 20; 
int i = sizeof(str)/sizeof(str[0]) // i = 10


// 字符串转换为数字
#include<stldlib.h>
char c = '9';
atoi(); // 把字符串转化为整形
atol(); // 把字符串转化为长整形
atof(); // 把字符串转化为双精度浮点型
int(c - '0'); // 直接减去'0'即可,可以不要int
