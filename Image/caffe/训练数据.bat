% 2018-7-21
% 参考链接 	https://blog.csdn.net/nichengwuxiao/article/details/79134977 # 下载训练数据
			https://blog.csdn.net/yanxiaopan/article/details/77485099
% 下载好的数据集分别为训练train和test文件， 将图片分别复制到caffe/data/mydata/train 和 caffe/data/mydata/test中
%% 1
% 数据标签生成
% caffe/data/mydata/generator.py
% 放在caffe/data/mydata/ 下 

import os
if __name__ == "__main__":

    dirs = ["train", "test"] # 训练测试文件夹名称
    data_dir = "C:/software/caffe/caffe-master/data/mydata/" # 依据自己创建路径修改

    for d in dirs:
        d_dir = data_dir + d
        dir_pre = d + "\\"
        file = d_dir + "/" + d + ".txt"
        d_file = open(file, "w")
        files = os.listdir(d_dir)
        index = 0
        for f in files:
            try:
            	# 例： test\305.jpg 0   此处图片路径与标签之间只能空了一格 否则转换数据时会出现错误，程序无法读取文件，导致均值无法生成
                d_file.write("{0}{1} {2}\n".format(dir_pre, f, int(f[0])-3))
            except:
                pass
            index += 1
            if index % 100 == 0:
                print("{0} processed".format(index))
        d_file.close()
    print("Successful")

%% 2
% 在caffe目录下创建mybat/mydata，以下bat脚本文件均保存在该目录下
%数据转换 data_transfer.bat
% 全路径 caffe/mybat/mydata/data_trnsfer.bat
..\..\Build\x64\Release\convert_imageset.exe --resize_height=32 --resize_width=32  --backend=leveldb ..\..\data\mydata\ ..\..\data\mydata\train\train.txt ..\..\data\mydata\trainldb
..\..\Build\x64\Release\convert_imageset.exe --resize_height=32 --resize_width=32  --backend=leveldb ..\..\data\mydata\ ..\..\data\mydata\test\test.txt ..\..\data\mydata\valldb
pause

%% 3
% 均值生成 mean_generator.bat
% 全路径 caffe/mybat/mydata/mean_generator.bat
..\..\Build\x64\Release\compute_image_mean.exe ..\..\data\mydata\trainldb --backend=leveldb ..\..\data\mydata\train_mean.binaryproto
..\..\Build\x64\Release\compute_image_mean.exe ..\..\data\mydata\valldb --backend=leveldb ..\..\data\mydata\val_mean.binaryproto
pause
