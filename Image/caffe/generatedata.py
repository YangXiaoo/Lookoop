# 2018-9-14
import os
import math


def main(dirs, data_dir, handle=True):
    """
    dirs: 训练数据与测试数据文件目录，list类型 dirs = ["train", "val"]
    data_dir： 训练数据与测试数据所在目录
    handle： 是否处理val\m-10-10.4 (2).png 这样带"()"的文件名, 默认处理该文件并生成标签
    handle=False：跳过该文件不处理
    """
    for d in dirs:
        d_dir = data_dir + d
        dir_pre = d + "\\"
        file = d_dir + "/" + d + ".txt"
        d_file = open(file, "w")
        files = os.listdir(d_dir)
        index = 0
        for f in files:
            s = f.split("-")[-1]
            year = s.split(".png")[0]
            # print(s.split(".png")[0])
            if '(' in year:
                year = year.split(" ")[0]
                # print("重复: ", year)
                if not handle:
                    continue
            try:
                year = round(float(year))
                d_file.write("{0}{1} {2}\n".format(dir_pre, f, year))
            except:
                pass
            index += 1
        d_file.close()
    print("Successful total: " + str(index))


if __name__ == "__main__":
    """
    Test!
    """
    dirs = ["train", "val"]
    data_dir = "C:/software/caffe/caffe-master/data/xunlian/"
    main(dirs, data_dir) # 处理带"()"的文件名
    # main(dirs, data_dir, handle=False) # 跳过带"()"的文件名
