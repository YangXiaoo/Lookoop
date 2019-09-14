# coding: utf-8
"""
转换文件中的中文格式
"""
import os
from util import getFiles

class Exg(object):
	def __init__(self, oldFilePath, outputFilePath=None, 
				 oldList=None, newList=None):
		"""初始化
		@param oldFilePath 必须填写
		"""
		self.filePath = oldFilePath
		self.outputFilePath = outputFilePath
		self.oldList = None
		self.newList = None
		self.addRegx(oldList, newList)


	def addRegx(self, oldList=None, newList=None):
		"""添加规则
		添加列表规则, 需对应： ["，", "？", "："], [", ", "? ", ": "]
		or 添加单个规则, 不用列表: addRegx("，", ", ")
		@param oldList 待替换的字符串
		@param newList 新字符串

		@return None
		"""
		if oldList == None or newList == None:
			return
		if not isinstance(oldList, list):	# 判断一个即可
			oldList = [oldList]
			newList = [newList]

		if not self.oldList:	# 只用判断一个就行
			self.oldList = oldList
			self.newList = newList
		else:
			self.oldList.extend(oldList)
			self.newList.extend(newList)

	def write(self, outputFilePath=None):
		if self.outputFilePath == None and outputFilePath == None:
			assert False, "确定输出路径"
			return 

		self.outputFilePath = outputFilePath

		newData = []
		with open(self.filePath, encoding="utf-8") as f:
			data = f.readlines()
			for line in data:
				for regxIndex, regx in enumerate(self.newList):
					line = line.replace(self.oldList[regxIndex], regx)
				newData.append(line)

		newFile = open(self.outputFilePath, "w", encoding="utf-8")
		newFile.write("".join(newData))
		newFile.close()


def mkfile(filePath, midffix=""):
	"""创建新文件路径，在文件名的后面,格式前面添加新的字符
	@param filePath 原文件路径
	@param midffix 文件名添加的字符
	
	@return 新文件路径
	"""
	fileDirName = os.path.dirname(filePath)
	fileBaseName = os.path.basename(filePath)
	filePreffix = fileBaseName.split(".")[0]
	fileSuffix = fileBaseName.split(".")[-1]
	outputFileName = os.path.join(fileDirName, filePreffix + midffix + "." + fileSuffix)

	return outputFileName

if __name__ == '__main__':
	fileDir = r"C:\Study\github\Lookoops\interview\src"
	fileList = getFiles(fileDir, None)
	for filePath in fileList:
		re = Exg(filePath)
		re.addRegx(["，", "？", "：", "；", '（', '）', "###", '”', '。'], [", ", "? ", ": ", "; ", '(', ')', "##", '"', '.'])
		re.write(filePath)