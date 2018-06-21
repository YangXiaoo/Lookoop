'''
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
解释: 
P   A   H   N
A P L S I I G
Y   I   R
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

# 2018-6-16

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        result = ""
        print(str_length,node_length)
        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):  # 从第一行遍历到最后一行
            for j in range(i, str_length, node_length):
                result += s[j]  # 第一行和最后一行  还有普通行的整列数字
                # i != 0 : 排除第一行
                # i != numRows-1 : 排除最后一行
                # j + node_length - 2*i < str_length ： 在字符串内
                if i != 0 and i != numRows-1 and j + node_length - 2*i < str_length:
                    result += s[j+node_length-2*i]  # 单列行的数字
                print(i,j)
        return result


# test
s = "PAYPALISHIRING"
r = 3
test = Solution()
re = test.convert(s,r)
print(re)