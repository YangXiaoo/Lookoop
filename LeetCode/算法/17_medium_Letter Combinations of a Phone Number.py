'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
2:abc
3:def
4:ghi
5:jkl
6:mno
7:pqrs
8:tuv
9:wxyz

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

# 2018-6-17
# Letter Combinations of a Phone Number
# 使用递归，可以改进
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {"0":"","1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        if len(digits) == 0:
            return []
        for i in dicts[digits[0]]:
            res.append(i)
        return self.handle(res,digits[1:],dicts)

    def handle(self,res,digits,dicts):
        if not digits:
            return res
        r = []
        for i in dicts[digits[0]]:
            for j in range(len(res)):
                r.append(res[j] + i)
        return self.handle(r,digits[1:],dicts)

# test
d = "23"
test = Solution()
res = test.letterCombinations(d)
print(res)