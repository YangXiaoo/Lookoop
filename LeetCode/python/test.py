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




class Tree(object):
	def __init__(self,l,r):
		self.l = l
		self.r = r
		self.value = 0
		self.left = None
		self.right = None
		if l < r:
			mid = (l + r)/2
			self.left = Tree(l,mid)
			self.right = Tree(mid+1,r)
 
	def set_value(self,p,value):
		if self.l == self.r:
			self.value = value
			return
		mid = (self.l + self.r)/2
		if p <= mid:
			self.left.set_value(p,value)
		else:
			self.right.set_value(p,value)
		self.push_up()
 
	def push_up(self):
		self.value = self.left.value + self.right.value
 
	def query(self,x,y):
		print "query",x,y,'\t',(self.l + self.r)/2,'\t',self.l,self.r,self.value
		if x <= self.l and y>=self.r:
			return self.value
		if self.l == self.r:
			return self.value
 
		mid = (self.l + self.r)/2
		if mid >= y:
			return self.left.query(x,y)
		elif mid < x:
			return self.right.query(x,y)
		else:
			return self.left.query(x,mid) + self.right.query(mid+1,y)
 
 
 
def main():
	N = 1024
	import time
	old =time.time()
	tree = Tree(0,N)
	for i in xrange(N+1):
		# print i
		tree.set_value(i,1)
	print tree.query(30,60)
	print time.time() -old
 
if __name__ == "__main__":
	main()
