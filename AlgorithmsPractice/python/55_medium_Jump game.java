class Solution {
    public boolean canJump(int[] nums) {
        int cur = 0;
        int i = 0;
        for (; i < nums.length; ++i) {
            if (nums[i] >= cur) {
                cur = nums[i];
            }
            if (cur == 0) {
                ++i;
                break;
            }
            cur = cur - 1;
        }
        
        return i == nums.length;
    }
}