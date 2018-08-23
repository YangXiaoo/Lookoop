# 2018-8-23
# 有限自动机进行字符串匹配

# 算法导论 P583
# 有限状态机介绍： https://blog.csdn.net/tyler_download/article/details/52549315
# 算法数学介绍： https://blog.csdn.net/tyler_download/article/details/52691243

"""
一个有限自动机 M 是一个5元组（Q, q0，A, Σ, δ），其中： 
Q是所有状态的有限集合;
q0∈Q (属于)是初始状态;
A⊆Q 是一个特殊的接受状态集合;
Σ 是有限输入字母表;
δ 是从Q * Σ到Q的转移函数，称为有限自动机M的转移函数;
"""