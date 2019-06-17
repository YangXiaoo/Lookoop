# coding=uft-8

"""
01背包
有N件物品和一个容量为V的背包。第i件物品的价格（即体积，下同）是w[i]，价值是c[i]. 
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
"""

# https://blog.csdn.net/weixin_39059738/article/details/79924049
def ans():
	"""
	分两种情况
		1. 不放入背包 f[i-1][v]
		2. 放入背包 max(f[i-1][v], f[i-1][v-w[i]] + v[i])
