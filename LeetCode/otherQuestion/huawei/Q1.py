# coding:utf-8
# 输出长度不超过255
# 报文转义，没有读懂题目
import sys
def solver(nums):
    ret = []
    for n in nums:
        if n == 'A':
            ret.extend(["12", "34"])
        elif n == 'B':
            ret.extend(["AB", "CD"])
        else:
            ret.append(n)
            
    lens = [str(len(ret) + 1)]
    lens.extend(ret)
    return lens

def test():
    line = "1"
    lines = line.split(" ")
    nums = lines[1:int(lines[0])]
    # print(nums)
        
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test() 
    s = "as"
