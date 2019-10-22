// 2019-3-20
#include <stdio.h>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

/* 
 * 替换空格
 * 
 * 请实现一个函数，把字符串中的每个空格替换成"%20"。例如
 * 输入 "we are happy"
 * 输出 "we%20are%20happy"
 *
 * 空格的ASCII码是32，即十六进制的0x20, 在URL中替换为%20
 * '#' 的ASCII码为35，即十六进制的0x23，在URL中替换为%23
 */


/**
 * 由前向后时间效率为O(n2), 由后向前则为O(n)
 * 由后向前查找替换  (c)
 */
void replaceBlank(char string[], int length) {
	if (string == nullptr || length <= 0) return;

	// 获取字符串实际长度与空白符的长度
	int old_size = 0, blank_size = 0, i = 0;
	while (string[i] != '\0') {
		++old_size;
		if (string[i] == ' ')
			++blank_size;
		++i;
	}

	int new_size = old_size + blank_size * 2;	// 新字符串长度
	if (new_size > length)	// new_size + 1 > length
		return;

	int index = new_size;
	while (index >= 0 && old_size < index) {
		if (string[old_size] == ' ') {
			string[index--] = '0';
			string[index--] = '2';
			string[index--] = '%';
		} else {
			string[index--] = string[old_size];
		}

		--old_size;
	}
}

void test(const char* test_name, char string[], int length, const char truth[]) {
	printf("caling %s\n", test_name);
	replaceBlank(string, length);

	printf("%s\n", string);

	if (truth == nullptr && string == nullptr) 
		printf("passed.\n");
	else if (truth == nullptr && string != nullptr)
		printf("failed.\n");
	else if (strcmp(string, truth) == 0)
		printf("passed.\n");
	else
		printf("failed.\n");
}

void test1() {
	const int length = 100;
	char string[length] = "we are happy";
	test("test1", string, length, "we%20are%20happy");
}

void test2()
{
    const int length = 100;

    char string[length] = " ";
    test("test2", string, length, "%20");
}



int main(int argc, char const *argv[])
{

	test1();
	test2();
	return 0;
}
// output:
// caling test1
// we%20are%20happy
// passed.
// caling test2
// %20
// passed.
