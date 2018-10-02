# 2018-9-5
# update on 2018-9-7 : 跳过test和笔记文件
# update on 2018-9-13 : 统计easy, medium, hard
# 统计LeetCode已做题目数量
import os
__easy_tag = ["easy", "simple"]
__medium_tag = ["medium"]
__hard_tag = ["hard", "diffcult"]
__tag = ["easy", "medium", "hard"]


def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
    return file


def handle(files):
    res = []
    suffix = [".py", ".c", ".cpp", ".java", ".sql"]
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


def printFile(files,prin=True):
    dic = {}
    excp = []
    for f in files:
        s = f.split("_")[0]
        if len(s) < 4:
            dic[s] = f
        else:
            excp.append(s)

    res = sorted(dic.keys())
    print("Total：", len(res))
    if prin:
        print("List:")
        for i in res:
            t = dic[i]
            print(t)

        print()
        for s in excp:
            print("Skip: ", s)
        

def classFile(files):
    easy, medium, hard = [], [], []
    for f in files:
        s = f.split("_")
        for c in s:
            if c in __easy_tag:
                easy.append(f)
                break
            if c in __medium_tag:
                medium.append(f)
                break
            if c in __hard_tag:
                hard.append(f)
                break

    return easy, medium, hard


def main():
    dirs = "C:\\Study\\github\\Lookoop\\LeetCode"
    files = file(dirs)
    res = handle(files)

    res = sortFile(res)
    printFile(res,False)
    print()
    # easy, medium, hard = classFile(res)
    clas = classFile(res)

    for i, r in enumerate(clas):
        print(__tag[i])
        printFile(r, False)


if __name__ == "__main__":
    main()
