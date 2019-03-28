// 2019-3-28
#include <stdio.h>
#include <vector>
using namespace std;

void ReorderOddEven(vector<int>& nums);
/* 使奇数位于偶数前面 */
void ReorderOddEven(vector<int>& nums) {
	if (nums.empty()) return;

	int start = 0, end = nums.size() - 1;

	while (start < end) {
		for (; nums[start] % 2 != 0 & start < nums.size(); ++start) {}
		for (; nums[end] % 2 == 0 & end > 0; --end) {}

		if (start >= end) break;

		int tmp = nums[start];
		nums[start] = nums[end];
		nums[end] = tmp;
		++start;
		--end;
	}
}


void test(const char* call_name, vector<int> nums, vector<int> expect) {
	printf("%s, result: ", call_name);

	ReorderOddEven(nums);
	for (auto n : nums) {
		printf("%d\t", n);
	}
	if (nums == expect)
		printf("passed.\n");
	else
		printf("failed.\n");
}

int main(int argc, char const *argv[])
{
	test("test1", { 1, 2, 3, 4 }, { 1, 3, 2, 4 });
	test("test2", { 1, 3, 2, 4 }, { 1, 3, 2, 4 });
	test("test3", { 1, 3, 2, 4, 5, 6, 7 }, { 1, 3, 7, 5, 4, 6, 2 });
	test("test4", { 1, 3, 2, 4, 5, 6, 7 }, { 1, 3, 7, 5, 2, 6, 4 });
	return 0;
}

// print 
// test1, result: 1        3       2       4       passed.
// test2, result : 1        3       2       4       passed.
// test3, result : 1        3       7       5       4       6       2       passed.
// test4, result : 1        3       7       5       4       6       2       failed.