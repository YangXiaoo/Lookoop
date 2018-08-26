/**
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
*/

// 2018-7-30
//  
// https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/


// https://www.cnblogs.com/bywallance/p/5761269.html
// https://blog.csdn.net/wdlsjdl2/article/details/51714211?locationNum=5&fps=1

#include <stdio.h>

int maximumGap(int* nums, int numsSize);

int main()
{
  int nums[4] = {3,6,9,1};
  int *num = nums;
  int gap;
  gap = maximumGap(num, 4);
  printf("%d\n", gap); 
  return 0;
}

// Last executed input: [1,10000000]
int maximumGap(int* nums, int numsSize) {
    if (numsSize < 2) return 0;

    int min = nums[0];
    int max = nums[0];

    for (int i = 0; i < numsSize; i++)
    {
      min = min < nums[i] ? min : nums[i];
      max = max > nums[i] ? max : nums[i];
    }

    int buck[max + 1];
    for (int i = 0; i <= max; i++) buck[i] = 32767;
    for (int i = 0; i <= numsSize; i++) buck[nums[i]] = 1;

    int res[numsSize];
    int j = 0;
    for (int i = 0; i <= max; i++)
    {
      if (buck[i] == 1)
      {
        res[j] = i;
        j++;
      }
    }

    max = res[1] - res[0];
    for (int i = 2; i < numsSize - 1; i++)
    {
        max = res[i] - res[i - 1] > max ? res[i] - res[i - 1] : max;
    }

    return max;
}