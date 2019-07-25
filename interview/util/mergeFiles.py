# coding:utf-8
"""
@Author yangxiao.online
将多个md文件放到一起
"""
import os
import replaceChineseCharacer as rep


def getFiles(dirpath, suffix=["md"]):
    """获取指定目录下所有文件完整路径
    @param dirpath 目录
    @param suffix 文件格式

    @return list
    """
    fileList = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in suffix:
                fileList.append(path)
    return fileList


class MergeFile(object):
    def __init__(self, inputFilePath, outputFilePath=None):
        self.inputFileList = self.setInputFileList(inputFilePath)
        self.outputFilePath = outputFilePath

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

        return fileList

    def getData(self, filePath):
        retData = None
        with open(filePath, encoding="utf-8") as f:
            data = f.readlines();
            retData = data

        return retData

    def merge(self, outputFilePath=None):
        if outputFilePath == None and self.outputFilePath == None:
            assert False, "没有指定输出路径"
        if outputFilePath :
            self.outputFilePath = outputFilePath
        outputData = []
        print(self.inputFileList)
        for file in self.inputFileList:
            curData = self.getData(file)
            curData.append("\n---\n\n")
            outputData.extend(curData)
        # print(outputData)
        with open(self.outputFilePath, "w", encoding="utf-8") as outf:
            outf.write("".join(outputData))

if __name__ == '__main__':
    inputFilePath = r"C:\Study\github\Lookoops\interview\src"
    outputFilePath = r"C:\Study\github\Lookoops\interview\output.md"

    mergeTool = MergeFile(inputFilePath, outputFilePath)
    mergeTool.merge()

    re = rep.Exg(outputFilePath)
    re.addRegx("###", "-")
    re.writeInto(outputFilePath)














