class Solution {
    public int myAtoi(String str) {
        str = str.trim();       // remove whitespace
        long ret = 0;           // define return value
        if (str.length() == 0)  // check the str length
            return (int)ret;

        // check +/- sign
        boolean flag = true;    // positive integer
        int startIndex = 0;
        if (str.charAt(startIndex) == '-') {
            flag = false;
            ++startIndex;
        } else if (str.charAt(startIndex) == '+') {
            ++startIndex;
        }
        
        for (int i = startIndex; i < str.length(); ++i) {
            if (!Character.isDigit(str.charAt(i))) {    // if cur character is not a digit, break
                break;
            } else {
                ret = flag == true ? ret * 10 + (str.charAt(i) - '0') : ret * 10 - (str.charAt(i) - '0');
                if ((ret < Integer.MIN_VALUE) || (ret > Integer.MAX_VALUE)) {   // if ret is not in 
                    break;                                                      // the range, break
                }
            }
        }        
        
        // check the range
        if (ret > Integer.MAX_VALUE) {
            ret = Integer.MAX_VALUE;
        } else if (ret < Integer.MIN_VALUE) {
            ret = Integer.MIN_VALUE;
        }
        
        return (int)ret;
    }
}