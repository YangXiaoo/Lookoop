// 2019-3-24
#include <stdio.h>
#include <vector>
#include <cmath>

using namespace std;

int cuttingRope(int n) {
	if (n < 0) return -1;

	vector<int> result = {0, 1, 2};
	if (n <= 3)
		return result[n-1];

	int timesOf3 = n / 3;
	
	// 可以分为n个3与一个4
	if (n - timesOf3*3 == 1) {
		--timesOf3;
	}
	int timesOf2 = (n - timesOf3*3) / 2;

	return pow(3, timesOf3) * pow(2, timesOf2);
}

void test(const char* call_name, int n, int except) {
	printf("%s, result: ", call_name);

	int ret = cuttingRope(n);

	if (ret == except)
		printf("passed.\n");
	else
		printf("failed.\n");
}

int main(int argc, char const *argv[])
{
	test("test1", 3, 2);
	test("test2", 4, 4);
	test("test3", 5, 6);
	test("test4", 6, 9);
	test("test5", 7, 6);
	return 0;
}

// print:
// test1, result: passed.
// test2, result: passed.
// test3, result: passed.
// test4, result: passed.
// test5, result: failed.