class Solution {
    public int maxArea(int[] height) {
        int ret = 0;
        int left = 0, right = height.length - 1;
        while (left < right) {
            int curArea = (right - left) * Math.min(height[left], height[right]);
            if (curArea > ret) {
                ret = curArea;
            }
            if (height[left] > height[right]) {
                --right;
            } else {
                ++left;
            }
        }
        
        return ret;
    }
}