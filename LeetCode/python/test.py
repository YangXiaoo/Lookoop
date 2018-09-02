# test
# About using the 2 functions:-
# For update, pass index of location to be updated, input array, BIT, value to be added to original number
# i.e. new value - original value
# For getting sum of elements in range l to r,
# Getsum returns sum of elements from beginning to index
# Pass index, input array & BIT to function
# getsum of l to r = getsum of r - getsum of (l-1)

def update(index, a, tree, value):
# index is index to be updated, a is input array / list, tree is BIT array, value is value to be added to original 
# number at index location
    add = value
    n = len(a)
    while index<n:
        tree[index] += add
        index = index + (index & (-index))

def getsum(index, a, tree):
# index is location upto which you want the sum of elements from beginning
# tree is BIT[], a is input array / list
    n = len(a)
    ans  = 0
    while(index>0):
        ans += tree[index]
        index = index - (index & (-index))
    return ans

#Get the user input
# n = int( input("Number of Elements in array: "))
# inputArray = list(map(int, raw_input("Elements in array: ").split()))
inputArray = [1, 3, 5]
n = 3
inputArray.insert(0,0)                 # insert dummy node to have 1-based indexing

#Initialise Binary Indexed Tree to 0's considering that input array is all 0's
BIT = []
for i in range(0, n):
    BIT.append(0)

# Now we will construct actual BIT
# The 4th parameter is always an additional value which is to be added to element at index location
# since we have considered input array as 0 earlier (while initialising BIT), for updating, we will pass actual 
# value
for i in range(1, n):
    update(i, inputArray, BIT, inputArray[i])

k = 15
k = (k & -k)
b = 4
b = -b
print(k)

class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += nums[i]
                k += (k & -k)
        print(self.c)
        

    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i)
        print(self.c)

    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res
k = 3
while k > 0:
	print(k)
	k -= (k & -k)
print("________")
m = 2
while m < 7:
	print(m)
	m += (m & -m)