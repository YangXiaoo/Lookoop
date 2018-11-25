'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

# 2018-11-24
# 394. Decode String
# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, tmp_digit, index = [], '', []
        for k,v in enumerate(s):
            if v != ']':
                if v.isdigit():
                    tmp_digit += v
                    continue
                if v == '[':
                    index.append(len(stack))
                    stack.append(int(tmp_digit)) 
                    tmp_digit = ''
                stack.append(v)
            else:
                last = index.pop()
                # print(stack,  last)
                tmp = "".join(stack[last+2:]) * int(stack[last])
                # print(tmp, last, stack, index)
                del stack[last:]
                stack.append(tmp)

        # print(stack, index)
        return "".join(stack)

nums = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "3[w]", "100[leetcode]"]
test = Solution()
for s in nums:
    res = test.decodeString(s)
    print(res)

        