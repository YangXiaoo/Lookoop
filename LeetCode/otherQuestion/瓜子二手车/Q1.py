# coding:utf-8

import sys

def solver(nums):
    nums.sort()
    start = 1 
    for n in nums:
        if n >= 1:
            if n - start != 0:
                return start
                
            start += 1 
            

def inputs():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    
    ret = solver(nums)
    
    print(ret)
    
def test():
    nums = [3,4,-1,1]

    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test()