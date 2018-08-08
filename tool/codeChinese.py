#utf-8
# 2018-8-8
# Code chinese character
class CodeChar(object):
	"""
	Have code problem!
	test = CodeChar()
	res = test.code(string)
	res2 = test.decode(res)
	"""
	def __init__(self):
		self.exp = ['，','。','？','！','：','《','》','【','】','（','）','、','@','#','$','%','^','&','*','.',',','.','<','>','-','+','=']
		self.radix = 19
		self.a_int = 97
		self.A_int = 65

	def code(self, s):
		res = []
		for i in s:
			if i in self.exp:
				res.append(i)
			else:
				i_to_int = ord(i)
				if i_to_int > 19000 and i_to_int < 40000:
					nums = []
					while i_to_int > 0:
						num = i_to_int % 10
						nums.append(num)
						i_to_int = i_to_int // 10
						nums = nums[::-1]
						r = []
						fir = nums[0] * 10 + nums[1] - self.radix + self.A_int
						r.append(fir)
						sec = nums[2] + self.a_int
						r.append(sec)
						thr = nums[3] + self.a_int + 8
						r.append(thr)
						fur = nums[4] + self.a_int + 16
						r.append(fur)
						res.append("".join(r))
						r = []
		return "".join(res)

	def decode(self,s):
		record = []
		flag = 1
		re = ""
		for i in s:
			if i not iin self.exp:
				record.append(i)
			else:
				re += i
				flag = 0
			if flag == 0 and len(record) == 4:
				r = 0
				r += (ord(record[0]) - self.A_int + self.radixa) * 1000
				r += (ord(record[1]) - self.a_int) * 100
				r += (ord(record[2]) - self.a_int - 8) * 10
				r += ord(record[3]) - self.a_int - 16
				re += chr(r)
				record = []
				flag = 1

		res = ""
		pre = 0
		for i in re:
			if i == ' ' and pre == 1:
				res += i
			elif i != ' ':
				res += i
				pre = 0

			if i == ' ':
				pre = 1
		return res

s = """
终于有人在说话了！
好久不见，你在哪里。
嗯？
有人说：“上午个欧委会对我。”
【蛛丝】：我的手去和我。
"""
test = CodeChar()
r1 = test.code(s)
print(r1)