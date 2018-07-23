/**
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]                                  
Output: 4
*/

// 2018-7-23
// 136. Single Number
// 类似题目：很多成对出现数字保存在磁盘文件中，注意成对的数字不一定是相邻的，如2, 5,3, 4, 7,3, 4, 2,5……，由于意外有一个数字消失了，如何尽快的找到是哪个数字消失了？ 
// 异或满足交换规律 ：该题解析为 n = 4^1^2^1^2 --> n = 1^1^2^2^4 --> n = 0^0^4 --> n = 4
class 136_easy_Single_Number {
    public int singleNumber(int[] nums) {
        int n = 0
        for(int i = 0; i <= nums.length; i++) {
            n = n ^ nums[i];
        }
        return n;
    }
}