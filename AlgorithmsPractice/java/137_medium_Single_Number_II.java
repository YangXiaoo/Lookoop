/**
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
*/

// 2018-7-23
// 137. Single Number II
// https://www.cnblogs.com/yangrouchuan/p/5323327.html
// https://www.cnblogs.com/ganganloveu/p/4110996.html
class 137_medium_Single_Number_II {
    public int singleNumber(int[] nums) {
        hashMap<Integer, Integer> map = new hashMap<>();
        for (int i = 0; i < nums.length; i++) {
        	if (!map.containsKey(nums[i])) {
        		map.put(nums[i], 1);
			} else {
				map.put(nums[i], map.get(nums[i]) + 1);
			}
		}

		for (int i = 0; i < nums.length; i++) {
			if (map.get(nums[i]) != 3) return nums[i];
		}
    }
}