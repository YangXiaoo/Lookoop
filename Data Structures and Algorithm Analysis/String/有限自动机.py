# 2018-8-23 ~ 2018-8-24
# 有限自动机进行字符串匹配
# 杨潇 http://www.lxxx.site

# 算法导论 P583
# 有限状态机介绍： https://blog.csdn.net/tyler_download/article/details/52549315
# 算法推理： https://blog.csdn.net/tyler_download/article/details/52691243

"""
一个有限自动机 M 是一个5元组（Q, q0，A, Σ, δ），其中： 
Q是所有状态的有限集合;
q0∈Q (属于)是初始状态;
A⊆Q 是一个特殊的接受状态集合;
Σ 是有限输入字母表;
δ 是从Q * Σ到Q的转移函数，称为有限自动机M的转移函数;
"""

class AutomationMatcher(object):
	def __init__(self, P):
		self.P = P # 匹配模式
		self.jumpTable = {} # 状态表
		self.alpha = self.getAlpha() # 获得P中含有的字符(已排序)


	def getAlpha(self):
		"""
		获得匹配串中字符
		"""
		sets = []
		for i in self.P:
			if i not in sets:
				sets.append(i)
		return sorted(sets)


	def makeJumpTable(self):
		"""
		获得状态转移表
		"""
		m = len(self.P)

		for q in range(m+1): # 加上初始状态共有m+1种状态
			for k in self.alpha:
				Pq = self.P[:q] + k # 与下一个输出组成字符串
				nextState = self.findSuffix(Pq) # 下一个字符输入后匹配到的最长后缀长度即为下一次的状态
				if q not in self.jumpTable:
					self.jumpTable[q] = {}
				self.jumpTable[q][k] = nextState # 最后存储的形式为 {0:{'a':1,'b':0,'c':0},1:{'a':1,'b':2','c':0} ...}


	def findSuffix(self, Pq):
		"""
		获得Pq后缀与P前缀的最长匹配长度
		ababaa 与 ababaca的最长匹配长度为1 
			 |	  |    
		还可以简化，但这样更好理解  
		"""
		lens = len(Pq)
		suffixLens = 0
		dummy = 0
		while dummy < lens:
			if self.P[:dummy + 1] != Pq[lens - dummy - 1:]:
				dummy += 1
			else:
				dummy += 1
				suffixLens = dummy

		return suffixLens

	def match(self, T):
		"""
		对字符串T进行匹配
		"""
		lenP = len(self.P)
		q = 0 # 输出状态
		for k in T:
			maps = self.jumpTable.get(q)
			oldState = q
			q = maps.get(k)
			if q == None:
				q = 0
				print("Skip a character \"%s\", continue to match..." % k)
				continue
			print("Recive : %s , state from %d jump to %d" % (k, oldState, q) )

			if q == lenP:
				print("Successful!")
				return True

		print("Fail...")
		return False




def test():
	P = "ababaca"
	T = "abababacmabaaba"
	test = AutomationMatcher(P)
	test.makeJumpTable()
	print("jump table : ", test.jumpTable.values())
	test.match(T)



if __name__ == '__main__':
	test()