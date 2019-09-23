# coding:utf-8
"""
@Author yangxiao.online
将多个md文件放到一起
"""
import os
import replaceChineseCharacer as rep
from util import getFiles

class MergeFileHander(object):
    def __init__(self, inputFilePath, outputFilePath=None):
        self.inputFileList = self.setInputFileList(inputFilePath)
        self.outputFilePath = outputFilePath
        self.count = 0
        self.outputData = []    # 数据缓存

    def setInputFileList(self, inputFilePath):
        """获得待合并文件路径"""
        if inputFilePath == None:
            assert False, "指定路径不存在"
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
        """对`1-xx.md`格式文件根据序号进行升序"""
        # 排序
        tmpDict = {}
        for f in data:
            try:
                tmpDict[int(os.path.basename(f).split('-')[0])] = f 
            except Exception as e:
                print("[error] info:{}".format(e))


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
                if '##' in line.lstrip():
                    self.count += 1
                if len(line.strip()) > 0 and line.strip()[0] == ">":
                    retData.append("\n")
                if len(line.lstrip()) == 0:
                    preLine = retData[-1].strip()
                    if preLine[0] == ">":
                        retData.append(line)
                elif ("##" in line.lstrip() or "---" in line.lstrip()) and not flag:
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
            assert False, "保存路径不存在"
        if outputFilePath :
            self.outputFilePath = outputFilePath
        for file in self.inputFileList:
            curData = self.getData(file)
            curData.append("\n---\n\n")
            self.outputData.extend(curData)
        with open(self.outputFilePath, "w", encoding="utf-8") as outf:
            outf.write("".join(self.outputData))

        print("[INFO] question count: {}".format(self.count))
        print("[INFO] write successful!")


class MergeFile(MergeFileHander):
    def __init__(self, inputFilePath, outputFilePath=None):
        super(MergeFile, self).__init__(inputFilePath, outputFilePath)

    def addHeader(self, text):
        """在头部添加字段"""
        self.outputData.append(text)

if __name__ == '__main__':
    inputFilePath = r"C:\Study\github\Lookoops\interview\src"
    outputFilePath = r"C:\Study\github\Lookoops\interview\README.md"
    headerText = """> 关于Java基础知识，JVM，多线程，计算机网络，数据库，分布式，算法，Java框架，测试，Linux等知识，详细答案见`/src/`目录下的细分内容，里面附有面经\n"""

    mergeTool = MergeFile(inputFilePath, outputFilePath)
    mergeTool.addHeader(headerText)
    mergeTool.merge()

    re = rep.Exg(outputFilePath)
    re.addRegx(["，", "？", "：", "；", '（', '）',  '”', '。', "##", "> -"], [", ", "? ", ": ", "; ", '(', ')', '"', '.', "-", "> ##"])
    re.write(outputFilePath)
# [INFO] question count: 630
# [INFO] write successful!