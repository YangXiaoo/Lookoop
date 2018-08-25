'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''

# 2018-6-19
# Longest valid Parenthese
# 暴力破解(超出时间限制)
class Solution1:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dicts = {")":"(","(":"#"}
        r = []
        res = []
        index = []
        res.append(0)
        k = 0
        i = 0
        while i < len(s):
            if dicts[s[i]] in r:
                k += 2
                r.pop()
                index.pop()                
            else:
                index.append(i)
                r.append(s[i])
            res.append(k)
            i += 1
        res.pop(0)
        index.append(i-1)
        print(r,k,maxs,res,index)
        if len(index) == 1:
            return res[-1]
        n = 0
        node = []
        node.append(res[index[0]]-res[0])
        while n < len(index)-1:
            node.append(res[index[n+1]]-res[index[n]])
            n += 1
        print(node)
        return max(node)   


class Solution2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """        
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else: # 可以不需要else判断
                    stack = [0]
            # print(c,longest,stack)

        return longest
# s = ")()((()()(())"
# s = ""
s = "())))((())(())()(("
test = Solution2()
res = test.longestValidParentheses(s)
print(res)
