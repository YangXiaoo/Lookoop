class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int charNum[127];
        fill(charNum, charNum+127, -1);
        int start = -1, ret = 0;
        for (int i = 0; i < s.size(); ++i) {
            int curValue = s[i] - ' ';
            int oldIndex = charNum[curValue];
            charNum[curValue] = i;
            
            if ((oldIndex != -1) && (oldIndex > start)) {
                start = oldIndex;
            }
            
            if (i - start > ret) {
                ret = i - start;
            }
        }
        
        return ret;
    }
};