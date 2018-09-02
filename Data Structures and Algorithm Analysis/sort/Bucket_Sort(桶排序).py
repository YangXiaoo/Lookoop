# 2018-8-5 ~ 2018-8-6
# Bucket Sort

# Reference
# Introduction to Algorithms [P112]
# Data Structures and Algorithm Analysis in C [P189]
# https://www.cnblogs.com/shihuc/p/6344406.html

class BucketSort(object):
    """
    1. Define the data mapping function f(x) according to the data type
    2. Plan the data separately into the bucket
    3. Sort the bucket based on sequence number
    4. Sort the data in each bucket (fast row or other sorting algorithm)
    5. Map the sorted data to the original input array as output
    """
    def __init__(self, A, m = 33):
        self.A = A # Integer Arrary
        self.lens = len(A)
        self.m = m 
        self.bucket = {}

    def sort(self):
        self.putIntoBucket()
        nums = self.sortBucket()
        # print(nums)
        return self.merge(nums)


    def putIntoBucket(self):
        for n in self.A:
            m = self.getBuck(n)
            if m in self.bucket:
                self.bucket[m].append(n)
            else:
                self.bucket[m] = [n]

    def getBuck(self, n):
        try:
            n = int(n) % self.m
        except:
            sums = 0
            for i in n:
                sums += ord(i)
            n = ord(sums) % self.m
        return n

    def sortBucket(self):
        num = [] # store the bucket number
        for i in self.bucket:
            num.append(i)
        func = QuickSort(num)
        nums = func.quickSort()

        for n in nums:
            f = QuickSort(self.bucket[n])
            nu = f.quickSort()
            self.bucket[n] = nu
        return nums

    def merge(self, nums):
        res = self.bucket[nums[0]]
        i = 1
        while i < len(nums):
            tmp = []
            cur = self.bucket[nums[i]]
            while len(res) > 0 and len(cur) > 0:
                if res[0] <= cur[0]:
                    tmp.append( res.pop(0) )
                else:
                    tmp.append( cur.pop(0) )
            tmp += res
            tmp += cur
            res = tmp
            i += 1
        return res


class QuickSort(object):
    """
    Quick Sort
    """
    def __init__(self, A):
        self.A = A
        self.lens = len(A)

    def swap(self, a, b):
        tmp = self.A[a]
        self.A[a] = self.A[b]
        self.A[b] = tmp

    def findPivot(self, left, right):
        mid = (left + right) / 2
        self.swap(mid, right)

        boundary = left
        for index in range(left, right):
            if self.A[index] < self.A[right]:
                self.swap(boundary, index)
                boundary += 1
        self.swap(boundary, right)

        return boundary

    def quickSort(self):
        self.quicksortHelper(0, self.lens - 1)
        return self.A

    def quicksortHelper(self, left, right):
        if left < right:
            pivot = self.findPivot(left, right)
            self.quicksortHelper(left, pivot - 1)
            self.quicksortHelper(pivot + 1, right)
 

lists = [5,2,8,4,3,7,6,9,1,10,13,21,34,132]
test = BucketSort(lists)
re = test.sort()
print(re)