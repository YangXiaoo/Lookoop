# coding:UTF-8
# 2019-1-5
# data augmentation
# 还需要添加色度变换

import os
import numpy as np 
import random
import datetime
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


__suffix__ = ["png"]

def getFiles(dirpath):
    """
    获取文件
    """
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix__:
                file.append(path)
    return file


def printToConsole(start_time, f, count, total, gap):
    """
    打印信息
    """
    print("handled: ", f.split("\\")[-1])
    if count % gap == 0 and count != total:
        end_time = datetime.datetime.now()
        expend = end_time - start_time
        print("\nexpend time:", expend, "\nexpected time: ", expend / count * total, '\n')

    return 


def saveError(e, out_dir, f):
    """
    当出现错误时打印错误并保存未处理的图片到指定目录
    """
    print("Error: " + str(e))    
    failed_dir = os.path.join("\\".join(out_dir.split("\\")[:-1]), out_dir.split("\\")[-1] + "_failed")
    print("failed to handle %s, skiped.\nsaved in %s" % (f,failed_dir))
    if not os.path.isdir(failed_dir):
        os.mkdir(failed_dir)
    print(os.path.join(failed_dir, f.split("\\")[-1]))
    os.system("copy %s %s" % (f, os.path.join(failed_dir, f.split("\\")[-1])))

    return 


datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
)


def loadImg(pic_file):
    img = load_img(pic_file)
    img = img_to_array(img)
    img = img.reshape((1,) + img.shape)
    return img


def mkdir(file_list):
    for f in file_list:
        if not os.path.isdir(f):
            os.mkdir(f)
    return 


def cleanDir(tmp_dir):
    files = getFiles(tmp_dir)
    for f in files:
        os.remove(f)
    return 


def genPic(img, max_gen=50, **data):
    i = 0
    for batch in datagen.flow(img, **data):
        i += 1
        # print("generate: %s" % (i))
        if i > max_gen:
            break  # 否则生成器会退出循环
    return 


def getLables(tmp_lable_container, lable, pic_files):
    files = getFiles(pic_files)
    for f in files:
        base_name = os.path.basename(f)
        tmp_lable_container.append(base_name + ' ' + lable + '\n')

    return 


def movePic(tmp_dir, output_path):
    if os.path.isdir(tmp_dir):
        files = getFiles(tmp_dir)
        for f in files:
            dummy_smg = os.popen("copy %s %s" % (f, os.path.join(output_path, os.path.basename(f))))
    else:
        dummy_smg = os.popen("copy %s %s" % (tmp_dir, os.path.join(output_path, os.path.basename(tmp_dir))))
    return 


def getLablesDict(lable_path):
    lable = open(lable_path)
    data = lable.readlines()
    ret = {}
    for line in data:
        # print(line[:-1].split(' ')) # ['mm', '(2).png', '10']
        tmp = line[:-1].split(' ')
        key, value = ''.join(tmp[:-1]), tmp[-1]
        ret[key] = value
    lable.close()
    return ret


def augmentation(input_path, 
                output_path, 
                lables, 
                lable_output_path,
                batch_size=1,
                save_prefix='bone',
                save_format='png'):
    """
    input_path: 待处理数据路径
    output_path: 输出路径
    lables: 待处理数据对应标签, {'pic_01.png':label_01, 'pic_02.png':label_02,...}
    lable_output_path: 重新生成的标签输出路径
    """
    files = getFiles(input_path)

    tmp_lable_container = [] # 存储标签
    start_time = datetime.datetime.now()
    total = len(files)
    tmp_dir = 'C:\\gen_pic_tmp' # 生成图片的路径
    fail, success, skip, count = 0, 0, 0, 0

    mkdir([output_path, lable_output_path, tmp_dir]) # 检查输出目录是否存在

    cleanDir(tmp_dir) # 清空缓存文件

    for i, f in enumerate(files):
        count += 1
        print(count, '/', total)
        # try:
        # 载入图片
        img = loadImg(f)
        tmp_dir_sub = os.path.join(tmp_dir, str(i))
        mkdir([tmp_dir_sub])

        # 生成图片
        input_par = {
            'batch_size':batch_size, 
            'save_to_dir':tmp_dir_sub, 
            'save_prefix':save_prefix, 
            'save_format':save_format
        }
        genPic(img, max_gen=10, **input_par)

        # 将缓存中的图片移动到指定目录
        movePic(tmp_dir, output_path)

        # 复制当前使用的图片至指定目录
        movePic(f, output_path)

        # 获得标签
        base_name = os.path.basename(f)
        getLables(tmp_lable_container, lables[base_name], tmp_dir)
        tmp_lable_container.append(base_name + ' ' + lables[base_name] + '\n')
        
        # cleanDir(tmp_dir) # 清空缓存文件

        # 打印信息到输出台
        printToConsole(start_time, f, count, total, 5)
        success += 1
        # except Exception as e:
        #     # 错误情况
        #     saveError(e, output_path, f)
        #     fail += 1

    # 打乱标签列表写标签
    random.shuffle(tmp_lable_container)
    with open(os.path.join(lable_output_path, 'lable.txt'), 'w') as lable_file:
        for line in tmp_lable_container:
            lable_file.write(line)


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" % (total, success, skip, fail, expend))
    cleanDir(tmp_dir)
    # os.rmdir(tmp_dir) # 删除缓存目录
    os.startfile(output_path)


if __name__ == '__main__':

    lable_path = r'C:\Study\test\kaggle-bonage\train-male\train.txt'
    lables = getLablesDict(lable_path)

    input_path =  r'C:\Study\test\kaggle-bonage\train-male'

    output_path = r'C:\Study\test\kaggle-bonage\test'
    lable_output_path = r'C:\Study\test\kaggle-bonage\test'
    augmentation(input_path, 
                output_path, 
                lables, 
                lable_output_path,
                batch_size=1,
                save_prefix='bone',
                save_format='png')