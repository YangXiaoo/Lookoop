// 2019-5-14
// Runtime: 1 ms, faster than 100.00% of Java online submissions for Reverse Integer.
// Memory Usage: 32.5 MB, less than 100.00% of Java online submissions for Reverse Integer.
class Solution {
    public int reverse(int x) {
        long ret = 0;
        while (x != 0) {
            ret = ret * 10 + x % 10;
            x /= 10;
        }
        if ((ret > Integer.MAX_VALUE) || (ret < Integer.MIN_VALUE)) {
            ret = 0;
        }
        return (int)ret;
    }
}