# coding:utf-8
# 2020-2-7
# 将数据写成csv格式

import sys
sys.path.append("../")

import trainModel as util 

csvDataSavingPath = "../data/samples-csv.csv"

def main():
	X, Y = util.getTrainData()
	header = "y1,z1,z2,x2,x3,force\n"

	text = header
	for k,v in enumerate(X):
		tmpText = ",".join(map(lambda x:str(float("%.4f" % x)), v))
		tmpText += ",{}\n".format(Y[k][0])
		text += tmpText

	with open(csvDataSavingPath, "w") as f:
		f.write(text)


if __name__ == '__main__':
	main()


