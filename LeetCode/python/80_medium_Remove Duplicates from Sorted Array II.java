class Solution {
    public int removeDuplicates(int[] nums) {
        int numsLength = nums.length;
        if (numsLength == 0) return 0;
        
        int pre = nums[0];  // previous number
        int dupCount = 1;
        int curIndex = 1;   // define return length
        for (int i = 1; i < numsLength; ++i) {
            if (nums[i] == pre) {
                ++dupCount;
            } else {
                dupCount = 1;
            }
            if (dupCount < 3) {
                nums[curIndex] = nums[i];
                ++curIndex;
            }
            
            pre = nums[i];
        }
            
        return curIndex;
    }
}