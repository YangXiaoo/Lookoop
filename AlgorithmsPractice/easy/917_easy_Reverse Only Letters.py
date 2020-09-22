"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
# 2020-9-17
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        tmpSeq = [0 for _ in range(len(S))]
        characterRecord = []
        for i, c in enumerate(S):
            if c.isalpha():
                characterRecord.append(c)
            else:
                tmpSeq[i] = c
        # print(characterRecord)
        for i, c in enumerate(tmpSeq):
            if c == 0:
                tmpSeq[i] = characterRecord.pop()
        return "".join(tmpSeq)

    def reverseOnlyLetters2(self, S: str) -> str:
        stack = []
        for i, c in enumerate(S):
            if c.isalpha():
                stack.append(c)

        ret = []
        for i, c in enumerate(S):
            if c.isalpha():
                ret.append(stack.pop())
            else:
                ret.append(c)

        return "".join(ret)
        
# test
S = "Test1ng-Leet=code-Q!"
test = Solution()
res = test.reverseOnlyLetters2(S)
print(res == "Qedo1ct-eeLg=ntse-T!")