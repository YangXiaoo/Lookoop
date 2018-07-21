% 2018-7-21
% 参考链接 	https://blog.csdn.net/nichengwuxiao/article/details/79134977 # 下载训练数据
			https://blog.csdn.net/yanxiaopan/article/details/77485099
% 下载好数据集分别为训练train和test文件， 复制到caffe/data/mydata/train 和 caffe/data/mydata/test中
% 数据标签生成 python文件
import os
 
if __name__ == "__main__":
    test_dir = 'C:/software/caffe/caffe-master/data/mydata/test'
    train_dir = 'C:/software/caffe/caffe-master/data/mydata/train'
    test_fid = open("C:/software/caffe/caffe-master/data/mydata/test/test.txt","w")
    train_fid = open("C:/software/caffe/caffe-master/data/mydata/train/train.txt","w")
    test_files = os.listdir(test_dir)
    train_files = os.listdir(train_dir)
    index = 0
    for ii, file in enumerate(test_files,1):
        # print(file[0])
        try:
        # 333.jpg 0 图片路径与标签之间只能空一格
            test_fid.write("{0}{1} {2}\n".format("test\\",file, int(file[0])-3))
        except:
            pass
        index = index + 1
        if index%100 == 0:
            print("{0} images processed!".format(index))
    # print("All images processed!")
    test_fid.close()

    index = 0
    for ii, file in enumerate(train_files,1):
        # print(file[0])
        try:
            train_fid.write("{0}{1} {2}\n".format("train\\",file, int(file[0])-3))
        except:
            pass
        index = index + 1
        if index%100 == 0:
            print("{0} images processed!".format(index))
    # print("All images processed!")
    train_fid.close()

% 在caffe下创建mybat/mydata 保存bat脚本文件
%数据转换 data_transfer.bat
..\..\Build\x64\Release\convert_imageset.exe --resize_height=32 --resize_width=32  --backend=leveldb ..\..\data\mydata\ ..\..\data\mydata\train\train.txt ..\..\data\mydata\trainldb
..\..\Build\x64\Release\convert_imageset.exe --resize_height=32 --resize_width=32  --backend=leveldb ..\..\data\mydata\ ..\..\data\mydata\test\test.txt ..\..\data\mydata\valldb
pause

% 均值生成 mean_generator.bat
..\..\Build\x64\Release\compute_image_mean.exe ..\..\data\mydata\trainldb --backend=leveldb ..\..\data\mydata\train_mean.binaryproto
..\..\Build\x64\Release\compute_image_mean.exe ..\..\data\mydata\valldb --backend=leveldb ..\..\data\mydata\val_mean.binaryproto
pause
