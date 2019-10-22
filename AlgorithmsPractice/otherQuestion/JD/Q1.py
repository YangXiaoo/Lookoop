# coding:utf-8
"""
合唱队的N名学生站成一排且从左到右编号为1到N，其中编号为i的学生身高为Hi。现在将这些学生分成若干组（同一组的学生编号连续），并让每组学生从左到右按身高从低到高进行排列，使得最后所有学生同样满足从左到右身高从低到高（中间位置可以等高），那么最多能将这些学生分成多少组？
输入：
4
2 1 3 2

输出：
2

补充样例
输入样例2
10
69079936 236011312 77957850 653604087 443890802 277126428 755625552 768751840 993860213 882053548
输出样例2
6

此时分组为：【69079936】【236011312 77957850】【653604087 443890802 277126428】 【755625552】 【768751840】【 993860213 882053548】调整顺序后即可满足条件
"""
import sys
import copy 

# AC 54%
def solver(nums):
    old = copy.deepcopy(nums)
    nums.sort() # 排序
    ret = 0
    i = 0
    while i < len(nums):
        if nums[i] == old[i]:
            ret += 1
            i += 1
        else:
            tmp = []
            start = i
            while i < len(nums):
                tmp.append(old[i])
                tmp.sort()
                i += 1
                if tmp == nums[start:i]:
                    ret += 1

    return ret

def test():
    nums = [1,6,2,6]
    ret = solver(nums)
    print(ret)

def inputs():
    n = input()
    line = input()
    nums = list(map(int, line.split(" ")))
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test()
