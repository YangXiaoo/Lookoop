# coding:utf-8
"""
有一个非常经典的概率问题，是一个袋子里面有若干个红球和若干个蓝球，两个人轮流取出一个球，谁先取到红球谁就赢了，当人的先后顺序和球的数量确定时，双方的胜率都可以由计算得到，这个问题显然是很简单的。

现在有一个进阶版的问题，同样是一个袋子里面有n个红球和m个蓝球，共有A，B，C三人参与游戏，三人按照A，B，C的顺序轮流操作，在每一回合中，A，B，C都会随机从袋子里面拿走一个球，然而真正分出胜负的只有A，B两个人，没错，C就是来捣乱的，他除了可以使得袋子里面减少一个球，没有其他任何意义，而A，B谁 先拿到红球就可以获得胜利，但是由于C的存在，两人可能都拿不到红球，此时B获得胜利。

输入
输入仅包含两个整数n和m,表示红球和蓝球的数量，中间用空格隔开。(0<=n,m<=1000)

输出
请你输出A获胜的概率，结果保留5位小数。（四舍五入）


样例输入
1 1
样例输出
0.50000

提示
输入样例2
3 4
输出样例2
0.62857
"""
# ac 27%
def solver(n, m):
    def genNums(n, m, cur):
        nonlocal tmp, total, dem, retA
        if m == 0 and n == 0:
            dem += 1
            if check(tmp):
                retA += 1
        else:
            for i in range(cur, total):
                p = ['A', 'B', 'C'][cur % 3]
                if n > 0:
                    tmp.append(p+'0')
                    genNums(n-1, m, i+1)
                    tmp.pop()
                if m > 0:
                    tmp.append(p+'1')
                    genNums(n, m-1, i + 1)
                    tmp.pop()
    tmp = []
    total = m + n
    dem = 0
    retA  = 0
    genNums(n, m, 0)

    ret = float('%.5f' % (retA / dem))
    

    return ret

def check(tmp):
    retA = 0
    for n in tmp:
        # print(n)
        if n[1] == '0' and n[0] == 'A':
            retA += 1
            break
        elif n[1] == '0' and n[0] == 'B':
            break

    return retA

def test():
    n, m = 3, 4
    ret = solver(n, m)
    print(ret)

def inputs():
    n, m = list(map(int, input().strip().split()))
    ret = solver(n, m)
    print(ret)

    
if __name__ == '__main__':
    test()