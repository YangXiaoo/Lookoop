# 2018-9-5
# update in 2018-9-7 : 跳过test和笔记文件
# 统计LeetCode已做题目数量
import os
def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
    return file

def handle(files):
    res = []
    suffix = [".py", ".c", ".cpp", ".java"]
    for f in files:
        file_suffix = os.path.splitext(f)[1]
        if file_suffix in suffix:
            res.append(f)

    return res
def sortFile(files):
    res = []
    for f in files:
        fname = f.split("\\")[-1]
        res.append(fname)
    return sorted(res)

def printFile(files):
    dic = {}
    excp = []
    for f in files:
        s = f.split("_")[0]
        if len(s) < 4:
            dic[s] = f
        else:
            excp.append(s)

    res = sorted(dic.keys())
    print("Total：", len(res), "\n\nList:")
    for i in res:
        t = dic[i]
        print(t)

    print()
    for s in excp:
        print("Skip: ", s)
        



def main():
    dirs = "C:\\Study\\github\\Lookoop\\LeetCode"
    files = file(dirs)
    res = handle(files)

    printFile(sortFile(res))


if __name__ == "__main__":
    main()
