# coding:utf-8
# 2020-2-7
# 将样本数据写成csv格式

import sys
sys.path.append("../")

import trainModel as util 

csvDataSavingPath = "../data/samples-csv.csv"

def main():
	X, Y = util.getTrainData()

	header = "Y1,Z1,Z2,X2,X3,Force\n"	# 列名
	text = header

	for k,v in enumerate(X):
		tmpText = ",".join(map(lambda x:str(float("%.4f" % x)), v))
		tmpText += ",{}\n".format(Y[k][0])
		text += tmpText

	with open(csvDataSavingPath, "w") as f:
		f.write(text)


if __name__ == '__main__':
	main()


