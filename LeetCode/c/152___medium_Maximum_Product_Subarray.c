/**
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/
// 2018-7-29
// 152. Maximum Product Subarray
#include <stdio.h>

int maxProduct(int * nums, int numsSize);

int main()
{
	int num[4] = {2,3,-2,4};
	int * nums = num;
	int max;
	max = maxProduct(nums, 4);
	printf("%d\n", max);
	return 0;

}
 
int maxProduct(int* nums, int numsSize) {
    if (numsSize == 1) return nums[0];

    int maxProduct = nums[0];
    int minProduct = nums[0];
    int res = nums[0]; // 记录最大相乘结果
    int tmp1,tmp2;

    for (int i = 1; i < numsSize; i++) 
    {
    	int a = maxProduct * nums[i];
    	int b = minProduct * nums[i];

    	tmp1 = a > b ? a : b;
    	maxProduct = nums[i] > tmp1 ? nums[i] : tmp1;

    	tmp2 = a < b ? a : b;
    	minProduct = nums[i] < tmp2 ? nums[i] : tmp2;

    	res =  maxProduct > res ? maxProduct : res;
    }

    return res;
}