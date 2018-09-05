# 2018-9-5
# 统计LeetCode已做题目数量
import os
def file(dirpath):
    file = []
    direction = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
        for p in dirs:
            direction.append(p)
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
    for f in files:
        s = f.split("_")[0]
        dic[s] = f

    res = sorted(dic.keys())
    # print(res)
    for i in res:
        t = dic[i]
        print(t)
        



def main():
    dirs = "C:\\Study\\github\\Lookoop\\LeetCode"
    files = file(dirs)
    res = handle(files)
    print("共计：", len(res), "题")
    printFile(sortFile(res))


if __name__ == "__main__":
    main()
