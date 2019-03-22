// 2019-3-22
#include <stdio.h>
#include <vector>
#include <exception>
#include <stack>

using namespace std;

/**
 * 旋转数组的最小数字
 * 把一个数组最开始的若干元素搬到数组的末尾，称之为数组的旋转。
 * 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
 */

int minSequence(vector<int>& nums, int start, int end);

int minNumber(vector<int>& nums) {
	if (nums.empty())
		return -1;

	int start = 0, end = nums.size() - 1, mid = 0;
	while (start <= end) {
		
		if (end - start == 1) {
			mid = end;
			break;
		}
		int mid = start + ((end - start) >> 1);

		if (nums[start] == nums[end] && nums[start] == nums[mid]) {
			return minSequence(nums, start, end);
		}
		if (nums[mid] > nums[start]) {
			start = mid;
		} else if (nums[mid] <= nums[end]) {
			end = mid;
		}
	}

	return nums[mid];
}

int minSequence(vector<int>& nums, int start, int end) {
	int min = nums[start];

	for (++start; start<=end; ++start) {
		if (nums[start] < min) 
			min = nums[start];
	}

	return min;
}


void test(const char* call_name, vector<int>& nums, int except) {
	printf("call test name: %s, result: ", call_name);

	int ret = minNumber(nums);

	if (ret == except) {
		printf("passed.\n");
	else
		printf("failed.\n");
	}
}

int main(int argc, char const *argv[])
{
	vector<int> nums1 = {3, 4, 5, 1, 2};
	vector<int> nums2 = {1, 0, 1, 1, 1};

	test("test1", nums1, 1);
	test("test2", nums2, 0);
	return 0;
}

// print:
// call test name: test1, result: passed.
// call test name: test2, result: passed.