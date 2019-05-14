class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] charNum = new int[127];
        Arrays.fill(charNum, -1);
        
        int start = -1;     // start index
        int ret = 0;        // define maxLength
        for (int i = 0; i < s.length(); ++i) {
            int curValue = s.charAt(i) - ' ';
            int oldIndex = charNum[curValue];
            charNum[curValue] = i;
            
            if ((oldIndex != -1) && (oldIndex > start)) {
                start = oldIndex;
            }
            if ((i - start) > ret) {
                ret = i - start;
            }
        }
        
        return ret;
    }
}