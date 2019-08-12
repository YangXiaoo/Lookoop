# coding:utf-8
"""
@Author yangxiao.online
将多个md文件放到一起
"""
import os
import replaceChineseCharacer as rep
from util import getFiles

class MergeFile(object):
    def __init__(self, inputFilePath, outputFilePath=None):
        self.inputFileList = self.setInputFileList(inputFilePath)
        self.outputFilePath = outputFilePath
        self.count = 0

    def setInputFileList(self, inputFilePath):
        """获得待合并文件路径"""
        if inputFilePath == None:
            assert False, "没有指定文件路径"
        fileList = []
        if not isinstance(inputFilePath, list):
            inputFilePath = [inputFilePath]

        for file in inputFilePath:
            if os.path.isdir(file):
                fileList.extend(getFiles(file))
            else:
                fileList.append(file)

        fileList = self.sortValue(fileList)

        return fileList

    def sortValue(self, data):
        """对`1-xx.md`格式文件对序号进行排序"""
        # 排序
        tmpDict = {}
        for f in data:
            tmpDict[int(os.path.basename(f).split('-')[0])] = f 

        tmpList = sorted(tmpDict.items(), key=lambda x : x[0])
        retData = []
        for f in tmpList:
            retData.append(f[1])

        return retData

    def getData(self, filePath):
        retData = []
        with open(filePath, encoding="utf-8") as f:
            data = f.readlines()
            flag = False
            for line in data:
                if '#' in line.lstrip():
                    self.count += 1
                if len(line.strip()) > 0 and line.strip()[0] == ">":
                    retData.append("\n")
                if len(line.lstrip()) == 0:
                    preLine = retData[-1].strip()
                    if preLine[0] == ">":
                        retData.append(line)
                elif ("#" in line.lstrip() or "---" in line.lstrip()) and not flag:
                    retData.append(line)
                else:
                    if "```" in line:
                        retData.append(line)
                        if flag == False:
                            flag = True
                        else:
                            flag = False
                    elif flag:
                        retData.append(line)



        return retData

    def merge(self, outputFilePath=None):
        if outputFilePath == None and self.outputFilePath == None:
            assert False, "没有指定输出路径"
        if outputFilePath :
            self.outputFilePath = outputFilePath
        outputData = []
        for file in self.inputFileList:
            curData = self.getData(file)
            curData.append("\n---\n\n")
            outputData.extend(curData)
        with open(self.outputFilePath, "w", encoding="utf-8") as outf:
            outf.write("".join(outputData))

        print("[INFO] question count: {}".format(self.count))
        print("[INFO] write successful!")

if __name__ == '__main__':
    inputFilePath = r"C:\Study\github\Lookoops\interview\src"
    outputFilePath = r"C:\Study\github\Lookoops\interview\README.md"

    mergeTool = MergeFile(inputFilePath, outputFilePath)
    mergeTool.merge()

    re = rep.Exg(outputFilePath)
    re.addRegx("###", "-")
    re.write(outputFilePath)

# [INFO] question count: 563
# [INFO] write successful!