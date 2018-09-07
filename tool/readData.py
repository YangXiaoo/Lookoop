# 2018-8-7
# read data from file
class ReadData(object):
	"""
	Usage:
		test = ReadData(filename)
		test.getKcol(2, force=True) to get K column data ingore string
		test.getKAvg(2, force=True) to get the average of k column data ingore string or other type
	"""
	def __init__(self, filename,):
		self.file = filename
		self.nums = []
		self.col = 0
		self.getCol()

	def getData(self):
		f = open(self.file,"r+")
		data = f.read();
		tmp = []
		res = []
		for i in data:
			if i != ' ' and i != '\n' and i != '\r':
				tmp.append(i)
			else:
				res.append(tmp)
				tmp = []
		self.nums = res

	def getCol(self):
		f = open(self.file,"r")
		data = f.read()
		col = 0
		for i in data:
			if i == '\n' or i == '\r':
				col += 1
				break
			elif i == ' ':
				col += 1
		self.col = col
		return col

	def getKCol(self, Kcol, force = False):
		self.getData()
		res = self.handle(Kcol, force)
		if res:
			return res
		else:
			return False

	def handle(self, Kcol, isForce):
		if Kcol > self.col:
			print("Input must less than the total column of file. Please check!")
			return False

		lens = len(self.nums)

		res = []
		i = 0
		for c in self.nums:
			if (i % self.col) == (Kcol - 1):
				tmp = "".join(self.nums[i])
				if isForce:
					try:
						res.append(int(tmp))
					except:
						print("Skip : ", tmp)

				else:
					try:
						res.append(int(tmp))
					except:
						print("Exists string or other type that can no trnsfer to Integer. Please use \"force=True\" inorder to get protype data.")
						return False
			i += 1

		return res

	def getKAvg(self, Kcol, force = False):
		data = self.getKCol(Kcol, force)
		if data:
			lens = len(data)
			sums = sum(data)
			return float(sums / lens)
		else:
			print("Fail to get average.")
			return False
			
if __name__ == "__main__":
	file = "read_test.txt"
	test = ReadData(file)
	res = test.getData()
	r1 = test.getKCol(3,True)
	avg = test.getKAvg(3)
	col = test.getCol()
	print(res,"----", col,"----", r1, "----", avg)
