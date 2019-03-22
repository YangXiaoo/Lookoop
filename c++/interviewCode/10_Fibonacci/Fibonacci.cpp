// 2019-3-22
#include <stdio.h>
#include <vector>
#include <exception>
#include <stack>

using namespace std;

int Fibonacci(int n) {
	int ret[2] = {0, 1};
	if (n < 2)
		return ret[n];

	int a = 0, b = 1, c, i = 2;
	while (i <= n) {
		c = a + b;
		a = b;
		b = c;
		++i;
	}

	return c;
}

void test(const char* call_name, int n, int except) {
	printf("%s, result: ", call_name);

	int ret = Fibonacci(n);

	if (ret == except)
		printf("passed.\n");
	else
		printf("failed.\n");
}

int main(int argc, char const *argv[])
{
	test("test1", 3, 2);
	test("test2", 5, 5);
	test("test3", 6, 8);
	test("test4", 7, 11);
	return 0;
}