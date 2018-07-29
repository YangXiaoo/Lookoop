/**
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
*/

// 2018-7-29
// 154. Find Minimum in Rotated Sorted Array II
// https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

#include <stdio.h>

int findMin(int* nums, int numsSize);

int main()
{
    int num[5] = {2,2,2,0,1};
    int * nums = num;
    int max;
    max = findMin(nums, 5);
    printf("%d\n", max);
    return 0;

}
 
int findMin(int* nums, int numsSize) {
    if (numsSize < 1) return -1;

    int min = nums[0];

    for (int i = 1; i < numsSize; i++)
    {
    	if (nums[i] < nums[i - 1]) 
    	{
    		min = nums[i];
    		break;
    	}
    } 
    return min;
}