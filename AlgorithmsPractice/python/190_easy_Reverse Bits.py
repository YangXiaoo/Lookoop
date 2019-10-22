'''
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
'''

# 2018-9-23
# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/


class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        inputs = str(bin(n)[2:])
        gap = 32 - len(inputs)
        while gap > 0:
            inputs = "0" + inputs
            gap -= 1

        return int(inputs[::-1], 2)

class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        flag = 1
        for i in range(32):
            tmpRet = n & flag
            ret <<= 1
            ret += tmpRet
            n >>= 1
        return ret

n = 43261596    # 964176192
test = Solution2()
res = test.reverseBits(n)
print(res)