# 2018-9-14
import os
import math
def main(dirs, data_dir, handle=True, preffix=True):
    """
    数据路径: C:/software/caffe/caffe-master/data/xunlian/val/m-10-10.4 (2).png
    dirs: 训练数据与测试数据目录，list类型 dirs = ["train", "val"]
    data_dir： 训练数据与测试数据所在目录路径
    handle： 是否处理m-10-10.4 (2).png 这样带"()"的文件名, 默认处理该文件并生成标签. 默认参数True,意思是可以不输入handle=True
    handle=False：跳过该文件不处理
    preffix=True : 添加所在目录val\m-10-10.4 (2).png, 默认参数True
    preffix=False : 不添加所在目录m-10-10.4 (2).png

    生成的标签分别保存在dirs中的目录下["train", "val"]即C:/software/caffe/caffe-master/data/xunlian/val/val.txt
    """
    count = 0
    for d in dirs:
        d_dir = os.path.join(data_dir, d)
        dir_pre = d + "/"

        file = os.path.join(d_dir, d + ".txt")
        d_file = open(file, "w")
        files = os.listdir(d_dir)
        
        for f in files:
            count += 1
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
                if preffix:
                    d_file.write("{0}{1} {2}\n".format(dir_pre, f, year))
                else:
                    d_file.write("{0} {1}\n".format(f, year))
            except:
                pass
            
        d_file.close()
    print("Successful total: " + str(count))


if __name__ == "__main__":

    dirs = ["train", "val"]
    data_dir = "C:/software/caffe/caffe-master/data/xunlian"
    main(dirs, data_dir, preffix=False) # 处理带"()"的文件名, 不添加所在目录
    # main(dirs, data_dir, preffix=True) # 处理带"()"的文件名, 添加所在目录
    # main(dirs, data_dir, handle=False) # 跳过带"()"的文件名, 不添加所在目录
    # main(dirs, data_dir, handle=False, preffix=False) # 跳过带"()"的文件名, 添加所在目录
