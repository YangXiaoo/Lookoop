class BIT:
    def __init__(self, n):
        self.arr = [0] * n
        self.n = n
        
    def q(self, i):
        i += 1
        r = 0
        while i > 0:
            r += self.arr[i - 1]
            i -= i & (-i)
        return r
    
    def u(self, i, d):
        i += 1
        while i <= self.n:
            self.arr[i - 1] += d
            i += i & (-i)

            
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nn = list(set(nums))
        nn.sort()
        r = {}
        for i, n in enumerate(nn):
            r[n] = i
        a, b = [0] * len(nums), BIT(len(nn))
        for i, n in enumerate(reversed(nums)):
            a[len(nums) - i - 1] = b.q(r[n] - 1)
            b.u(r[n], 1)
        return a