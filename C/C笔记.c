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


// 复制
char * strncpy(char *s1, char *s2, size_t n); // 不保证s2中的'\0'被复制
char * strcpy(char *s1, char *s2); // 若s2的长度小于s1的长度则会出现错误
将字符串s2中最多n个字符复制到字符数组s1中，返回指向s1的指针。
注意：如果源串长度大于n，则strncpy不复制最后的'\0'结束符，所以是不安全的，复制完后需要手动添加字符串的结束符才行。
Strcpy和Strncpy的区别- -
第一种情况：
char* p="how are you ?";
char name[20]="ABCDEFGHIJKLMNOPQRS";
strcpy(name,p); //name改变为"how are you ? "====>正确！
strncpy(name,p,sizeof(name)); //name改变为"how are you ? " ====>正确！
第二种情况：
char* p="how are you ?";
char name[10];
strcpy(name,p); //目标串长度小于源串,错误！
name[sizeof(name)-1]='\0'; //和上一步组合，弥补结果，但是这种做法并不可取，因为上一步出错处理方式并不确定
strncpy(name,p,sizeof(name)); //源串长度大于指定拷贝的长度sizeof(name)，注意在这种情况下不会自动在目标串后面加'\0'
name[sizeof(name)-1]='\0'; //和上一步组合，弥补结果
================================================
总结：strcpy
源字串全部拷贝到目标字串中,包括'\0'，但是程序员必须保证目标串长度足够，且不与源串重叠。
strncpy
如果目标长>=指定长>源长，则将源串全部拷贝到目标串，连同'\0'
如果指定长<源长，则将截取源串中按指定长度拷贝到目标字符串，不包括'\0'
如果指定长>目标长，错误!