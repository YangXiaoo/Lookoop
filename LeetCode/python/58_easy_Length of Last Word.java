class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        for (; end >= 0; --end) {
            if (s.charAt(end) != ' ') {
                break;
            }
        }
		
        int start = end;
        for (; start >= 0; --start) {
            if (s.charAt(start) == ' ') {
                break;
            }
        }
        
        return end - start;
    }
}