class Solution {
    public boolean isPalindrome(int x) {
        // check whether an integer is negative
        if (x < 0) {
            return false;
        }
        
        int xRec = x;
        long reverseInt = 0;
        while (x > 0) {
            reverseInt = reverseInt * 10 + x % 10;
            x /= 10;
        }
  
        return reverseInt == xRec;
        
    }
}