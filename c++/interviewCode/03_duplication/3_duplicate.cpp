#include <stdio.h>
#include <vector>
#include <iostream>

#include "util.hpp"		// 定义链表
using namespace std;
/**
 * 数组中重复的数组
 * Given an array nums containing n + 1 integers where each integer is between 1
 * and n (inclusive), prove that at least one duplicate number must exist. Assume
 * that there is only one duplicate number, find the duplicate one。
 *
 * You must not modify the array (assume the array is read only).
 * You must use only constant, O(1) extra space.
 * Your runtime complexity should be less than O(n2).
 * There is only one duplicate number in the array, but it could be repeated more
 * than once.
 */


/**
 * 修改原数组，不需要额外空间
 */
int findDuplicate_1(vector<int>& nums);	


/**
 * 使用二分法
 */
int findDuplicate_2(vector<int>& nums);	
int countRange(vector<int> &nums, int start, int end);	// helper

/**
 * 使用双指针
 */
int findDuplicate_3(vector<int>& nums);	



int main(int argc, char const *argv[])
{
	vector<int> nums = {1,3,4,2,2};
	int ret = -1;

	ret = findDuplicate_1(nums);
	printf("duplication number is %d\n", ret);

	ret = findDuplicate_2(nums);
	printf("duplication number is %d\n", ret);

	ret = findDuplicate_3(nums);
	printf("duplication number is %d\n", ret);

	return 0;
}


/**
 * 方法一 
 * 
 * 修改原数组
 * 当前索引的值与当前元素值不相同则替换，若替换过程中遇到同样的元素则出现重复
 */
int findDuplicate_1(vector<int>& nums) {
	for (int i = 0; i != nums.size(); ++i) {
		while (nums[i] != i) {
			int tmp_val = nums[i];
			if (nums[tmp_val] != tmp_val) {
				// swap
				int tmp = nums[i];
				nums[i] = nums[tmp];
				nums[tmp] = tmp;
			} else {
				return tmp_val;
			}
		}
	}

	return -1;
}


/**
 * 方法二
 *
 * 使用二分法
 */
int findDuplicate_2(vector<int>& nums) {
	int start = 1, end = nums.size() - 1;
	while (start <= end) {
		int mid = start + ((end - start) >> 1);
		int count = countRange(nums, start, mid);	// 获得指定范围内数字出现的次数
		// printf("range: [%d, %d], mid: %d, count: %d\n", start, mid, mid, count);
		if (end == start) {
			if (count > 1) 
				return start;
			else
				break;
		}

		if (count <= (mid - start + 1))
			start = mid + 1;
		else
			end = mid;
	}
}

int countRange(vector<int> &nums, int start, int end) {
	int count = 0;
	for (auto n : nums) {
		if (n >= start && n <= end) 
			++count;
	}

	return count;
}


/**
 * 方法三
 *
 * 使用双指针法
 */
int findDuplicate_3(vector<int>& nums) {
	int slow = nums[0], fast = nums[nums[0]];

	while (slow != fast) {
		slow = nums[slow];
		fast = nums[nums[fast]];
	}

	fast = 0;
	while (slow != fast) {
		fast = nums[fast];
		slow = nums[slow];
	}

	return slow;
}