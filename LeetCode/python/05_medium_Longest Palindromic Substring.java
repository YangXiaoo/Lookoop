// 2019-5-14
class Solution {
    public String longestPalindrome(String s) {
        int start = 0, maxLength = 0;
        for (int i = 0; i < s.length(); ++i) {
            if ((i - maxLength >= 0) && isPalindrome(s, i - maxLength, i)) {
                start = i - maxLength;
                maxLength += 1;
            }
            
            if ((i - maxLength >= 1) && isPalindrome(s, i - maxLength - 1, i)) {
                start = i - maxLength - 1;
                maxLength += 2;
            }
        }
        
        return s.substring(start, start + maxLength);
    }
    
    public boolean isPalindrome(String s, int start, int end) {
        while (start <= end) {
            if (s.charAt(start++) != s.charAt(end--)) {
                return false;
            }
        }
        
        return true;
    }
}