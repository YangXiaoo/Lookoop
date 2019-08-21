# coding:utf-8
# 分组转发，最后多少人能够收到消息
import sys
def solver(start, nums):
    dicts = set([start])
    for team in nums:
        for n in team:
            if n in dicts:
                dicts.update(set(team))
                # print(dicts)
                break

    ret = len(dicts)

    return ret

def test():
    start = "j"
    nums = [["j"],
            ["t", "d"],
            ["j"]]

    ret = solver(start, nums)

    print(ret)

if __name__ == '__main__':
    # line = "aj"
    # print(line.split(","))
    # dicts = set(["jj"])
    # for n in line.split(","):
    #     print(n)
    #     if n in dicts:
    #         print("true")
    test()
