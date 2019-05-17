class Solution {
    public String multiply(String num1, String num2) {
        String ret = "";
        int num1Length = num1.length();
        int num2Length = num2.length();
        int totalLength = num1Length + num2Length;
        int[] tmpRet = new int[totalLength];
             
        for (int i = num1Length - 1; i >= 0; --i) {
            int curIndex = totalLength - (num1Length - i);
            for (int j = num2Length - 1; j >=0 ; --j) {
                int curValue = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                tmpRet[curIndex] += curValue;
                --curIndex;
            }
        }
        
        int carry = 0;
        int m = totalLength - 1;
        while ((m >= 0) || (carry != 0)) {
            int pre = tmpRet[m];
            tmpRet[m] = (carry + pre) % 10;
            carry = (carry + pre) / 10;
            --m;
        }
        
        int start = 0;
        for (int n = 0; n < totalLength - 1; ++n) {
            if (tmpRet[n] == 0) {
                ++start;
            } else {
                break;
            }

        }
        
        for (int k = start; k < totalLength; ++k) {
            ret += tmpRet[k];
        }
        
        return ret;
        
    }
}