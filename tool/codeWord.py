# 2018-8-7
# code and decode english word

class CodeWord(object):
	def __init__(self,x):
		self.x = x
	def code(self, s):
		d = {}
		for i in (65,97):
			for j in range(26):
				d[chr(i+j)] = chr( (j+self.x) % 26 + i)
		res = "".join([d.get(c,c) for c in s])
		return res

	def deCode(self, s):
		d = {}
		for i in (65, 97):
			for j in range(26):
				d[chr(i+j)] = chr((j+26-self.x) % 26 + i)
		res = "".join([d.get(c,c) for c in s])
		return res


s = """
There are some people who think love is sex and marriage and six o'clock-kisses and children, and perhaps it is, Miss Lester.
But do you know what I think? I think love is a touch and yet not a touch.""" 
s2 = """
Kyviv riv jfdv gvfgcv nyf kyzeb cfmv zj jvo reu driizrxv reu jzo f'tcftb-bzjjvj reu tyzcuive, reu gviyrgj zk zj, Dzjj Cvjkvi.
Slk uf pfl befn nyrk Z kyzeb? Z kyzeb cfmv zj r kflty reu pvk efk r kflty.""" # 17

test = CodeWord(33)
r1 = test.code(s)
r2 = test.deCode(r1)
print(r1)
print(r2)