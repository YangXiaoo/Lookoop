class Solution {
    public int divide(int dividend, int divisor) {
        int sign = (((dividend > 0) && (divisor > 0)) || ((dividend < 0) && (divisor < 0))) ? 1 : -1;
        long _dividend = (long)dividend;
        long _divisor = (long)divisor;
        _dividend = Math.abs(_dividend);
        _divisor = Math.abs(_divisor);
        long ret = 0;
        while (_dividend >= _divisor) {
            int k = 0;
            long tmp = _divisor;
            while (_dividend >= tmp) {
                _dividend -= tmp;
                ret += 1 << k;
                k += 1;
                tmp <<= 1;
            }
        }
        
        ret = sign * ret;
        // System.out.println(ret);
        if (ret < Integer.MIN_VALUE) {
            ret = Integer.MIN_VALUE;
        }
        if (ret > Integer.MAX_VALUE) {
            ret = Integer.MAX_VALUE;
        }
        
        return (int)ret;
    }
}