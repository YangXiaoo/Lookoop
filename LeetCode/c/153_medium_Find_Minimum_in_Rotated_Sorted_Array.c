/**
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
*/

// 2018-7-29
// 153. Find Minimum in Rotated Sorted Array
// https://leetcode-cn.com/submissions/detail/4813199/

#include <stdio.h>

int findMin(int* nums, int numsSize);
int solution2(int * nums, int numsSize);
int solution3(int * nums, int numsSize);

int main()
{
    int num[5] = {3,4,5,1,2};
    int * nums = num;
    int max;
    max = findMin(nums, 4);
    printf("%d\n", max);
    max = solution2(nums,4);
    printf("%d\n", max);
    return 0;

}
 
int findMin(int* nums, int numsSize)
{
    if (numsSize < 1) return -1;

    int left = 0, right = numsSize - 1, mid = 0;
    while (nums[left] > nums[right])
    {
        if (right - left == 1) 
        {
            mid = right;
            break;
        }

        mid = left + (right - left) / 2;

        if (nums[mid] > nums[left])
        {
            left = mid;
        }
        else
        {
            right = mid;
        }
    }
    return nums[mid];
}

int solution2(int * nums, int numsSize)
{
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

int solution3(int * nums, int numsSize)
{
    if (numsSize < 1) return -1;
    int left = 0, right = numsSize - 1;
    if (nums[left] < nums[right]) return nums[i];
    int mid = (left + right) / 2;

    while (left + 1 < right)
    {
        if (nums[left] < nums[mid])
            left = mid;
        else
            right = mid;

        mid = (left + right) / 2;
    }

    return nums[right];
}