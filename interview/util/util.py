# coding:utf-8
import os

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
            if suffix == None:
                fileList.append(path)
            elif name.split(".")[-1] in suffix:
                fileList.append(path)
    return fileList