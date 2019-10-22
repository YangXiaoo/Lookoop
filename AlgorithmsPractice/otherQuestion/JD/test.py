# coding:utf-8
import sys
def solver(nums):
    ret = set([])
    for n in nums:
        ret.update(set(n))
    ret = list(ret)
    ret.sort()
    ret = map(str, ret)
    ret = " ".join(ret)
    
    return ret 

def test():
    nums = [[1,2],
            [1]]
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    # try:
    #     while True:
    #         _ = sys.stdin.readline().strip()
    #         nums = []
    #         for i in range(2):
    #             line = sys.stdin.readline().strip()
    #             cur = list(map(int, line.split(" ")))
    #             nums.append(cur)

    #         ret = solver(nums)
    # except:
    #     pass
    test()