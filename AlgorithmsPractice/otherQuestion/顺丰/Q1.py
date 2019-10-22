# coding:utf-8
"""
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
某学术会议上，一共有n个人参加，现在已知每个人会的语言（一个人可能不会任何语言）。现在有一种学习机，每一个学习机可以在会议期间使一个人暂时掌握一种自己不会的语言，问要使得任意两人都要能直接或者间接的交流至少准备多少个学习机？

间接交流的意思是：可以通过其他参加会议的人翻译（可能或出现很多人一起帮忙翻译的情况）进行交流。如：第一个人和第二个人会第一种语言，第二个人和第三个人会第二种语言，那么第一个人可以和第三个人进行交流（通过第二个人的翻译）

输入
第一行3个数n,m,k代表人数，语言数，已知的信息数 接下来k行，每行两个数u,v，代表u第个人会第v种语言

输出
输出需要准备的学习机的个数


样例输入
3 3 2
2 3
3 1
样例输出
2

提示
数据范围
1≤n≤100000 , 1≤m≤100000 , 0≤k≤100000 , 1≤u≤n , 1≤v≤m
"""
# AC 18%
def solver(n, m, k, language):
    """n,m,k代表人数，语言数，已知的信息数
    language: [[u, v]]  代表u第个人会第v种语言
    """
    people = [x+1 for x in range(n)]

    distinct = {}
    for re in language:
        u, v = re
        distinct[v] = distinct.get(v, 0) + 1

    # print(distinct)
    # print("[debug] cant:{}".format(cant))

    ret = 0
    suf = 0
    for key, val in distinct.items():
        ret += max(0, 2-val)    # 一门语言最少需要两个人
        if val >= 2:
            suf += 1

    ret += (len(distinct) - ret)
    return ret 

def test():
    n, m, k = 5, 5, 2
    language = [[2, 2],
                [3, 1],
                [1, 1]]

    ret = solver(n, m, k, language)
    print(ret)

def inputs():
    n, m, k = list(map(int, input().split(" ")))
    language = []
    for i in range(k):
        cur = list(map(int, input().split(" ")))
        language.append(cur)
        
    ret = solver(n, m, k, language)
    print(ret)

if __name__ == '__main__':
    test()