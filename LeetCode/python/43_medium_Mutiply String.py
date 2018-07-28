'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly
'''

# 2018-6-21
# Mutiply String
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # make sure size of num2 is bigger than size of num1
        if len(num1) > len(num2):
            return self.multiply(num2,num1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))
        k = 0
        c = 0
        for i in num1:
            k = c
            for j in num2:
                ans[k] += int(i) * int(j)
                k += 1
            c += 1
        c = 0
        i = 0
        #print(ans)
        for n in ans:
            ans[i] = (n+c)%10
            c = ((n+c)//10)
            i += 1
        res = ''
        flag = 0
        s = 0
        # print(ans)
        while ans[-1] == 0 and len(ans)>1:
            ans.pop(-1)
        for s in range(len(ans)-1,-1,-1):
            res += str(ans[s])
        return res



num1 = "123"
num2 = "456"
test = Solution()
res = test.multiply(num1,num2)
print(res)