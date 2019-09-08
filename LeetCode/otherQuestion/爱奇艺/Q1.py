# coding:utf-8
"""
给定一个长度为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？

输入
第一行包含一个整数N，1<N≤1000。

第二行包含N-1个空格隔开的整数A1到AN-1，0≤Ai≤1

输出
输出符合要求的排列个数对109+7取模后的结果。


样例输入
4
1 1 0
样例输出
3

提示
样例解释

符合要求的排列为{3 2 1 4}、{4 2 1 3}和{4 3 1 2}。
"""
# ac 36%
# leetcode 903
def solver(n, aNums):

    def generate(n, tmp, aNums):
        nonlocal ret
        if len(tmp) == n:
            ret += 1
        else:
            for i in range(1,n+1):
                if i not in tmp:
                    if check(tmp, i-1, aNums):
                        tmp.append(i)
                        generate(n, tmp, aNums)
                        tmp.pop()

    def check(tmp, i, aNums):
        if len(tmp) == 0:
            return True

        pre = tmp[-1]
        index = len(tmp)
        if aNums[index-1] == 0:
            if pre < i + 1:
                return True
        else:
            if pre > i + 1:
                return True

        return False

    ret = 0
    generate(n, [], aNums)
    # print(genNums)

    return ret

def solver(n, aNums):
    maxMod = 1e9 + 7
    dp = [[for x in range(i)]]


def test():
    n = 4
    aNums = [1,1,0]

    ret = solver(n, aNums)
    print(ret)


def inputs():
    n = int(input().strip())
    aNums = list(map(int, input().strip().split()))

    ret = solver(m, aNums)
    print(ret)

if __name__ == '__main__':
    test()
