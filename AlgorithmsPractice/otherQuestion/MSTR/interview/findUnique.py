# coding=utf-8
import sys 
""" 
1. We have an integer array where all the elements appear twice while only 1 elements appears once. Please find the 1 elements. [直接说出步骤，然后换成下面这道题]
2. We have an integer array where all the elements appear twice while only 2 elements appears once. Please find the 2 elements.

数组中只有两个数字只出现了一次，其余数字重复了两次，找出这两个数字
使用异或操作--最简单
面试官说不要使用异或操作，我想出来使用快排，然后面试官说对的，但细节有点问题
说了细节之后开始写代码
"""
# 代码有bug，没有完成
# 2019/8/27 17:03 完成
def findUnique(nums):
    ret = []
    left, right = 0, len(nums) - 1
    
    while True:
        boundary = quickHelper(nums, left, right)
        print("[debug] boundary: {}".format(boundary))
        retL = handle(nums, left, boundary+1)
        retR = handle(nums, boundary+1, right+1)
        print("[debug] retL: {}, retR: {}".format(retL, retR))
        # 1. left ret not equals 0
        if retL != 0:
            if retR != 0:
                ret.append(retL)
                ret.append(retR)
                break
            else:
                right = boundary
        # 2. right
        else:    # left ret equals 0
            left = boundary
        
    return ret 

def handle(nums, left, right):
    ret = 0
    for n in nums[left:right]:
        ret = ret ^ n 
        
    return ret 

def quickHelper(nums, left, right):
    mid = left + (left - right) >> 1
    nums[mid], nums[right] = nums[right], nums[mid]
    boundary = left 
    for i in range(left, right):
        if nums[i] <= nums[right]:
            nums[i], nums[boundary] = nums[boundary], nums[i]
            boundary += 1
            
    nums[boundary], nums[right] = nums[right], nums[boundary]    # exchange

    return boundary

def test():
    nums = [1,2,5,4,4,2,3,1]
    ret = findUnique(nums)
    print(ret)

if __name__ == '__main__':
    test()