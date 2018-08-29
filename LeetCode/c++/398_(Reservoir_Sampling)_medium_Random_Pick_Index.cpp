/* 
******************     水塘抽样(Reservoir Sampling)问题    ******************

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
===================================================================
*/
// 2018-8-29
// 398. Random Pick Index
// https://leetcode.com/problems/random-pick-index/description/
class Solution {
private:
	vector<int> nums;
public:
    Solution(vector<int> nums) {
        this->nums = nums;
    }
    
    int pick(int target) {
        int res;
        int i = 0;
        int lens = lens()
        for (vector<int>::iterator it=nums.begin(); it<nums.end(); it++)
        {
        	if (*it == target)
        	{
        		int j = rand() % i;
        		if (j == 0)
        			res = i;
        	}
        	i++;
        }

        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */