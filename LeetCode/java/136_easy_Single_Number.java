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
class 136_easy_Single_Number {
    public int singleNumber(int[] nums) {
        int n = 0
        for(int i = 0; i <= nums.length; i++) {
            n = n ^ nums[i];
        }
        return n;
    }
}