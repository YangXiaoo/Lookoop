# coding:UTF-8
# 2019-1-5
# data augmentation
# 还需要添加色度变换

import os
import numpy as np 
import random
import datetime
import shutil
import time
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
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 


def cleanDir(tmp_dir):
    files = getFiles(tmp_dir)
    for f in files:
        os.remove(f)
    return 


def genPic(img, max_gen=5, **data):
    i = 0
    for batch in datagen.flow(img, **data):
        i += 1
        # print("generate: %s" % (i))
        if i > max_gen:
            break  # 否则生成器会退出循环
    return 


def getlabels(tmp_lable_container, 
                lable, 
                pic_files, 
                file_dic):
    files = getFiles(pic_files)
    for f in files:
        f_dir, base_name = os.path.split(f)
        if base_name in file_dic:
            t = datetime.datetime.now()
            mid_name = str(t).split(' ')[-1].replace('.', '_').replace(':', '_')
            base_name = 'rename_' + mid_name + '_' + base_name
            print("[WARNING] file exist, rename file %s as %s" % (f, base_name))
            os.rename(f, os.path.join(f_dir, base_name))
        file_dic.append(base_name)
        tmp_lable_container.append(base_name + ' ' + lable + '\n')

    return file_dic
    

def movePic(tmp_dir, output_path):
    if os.path.isdir(tmp_dir):
        files = getFiles(tmp_dir)
        for f in files:
            dummy_smg = os.popen("copy %s %s" % (f, os.path.join(output_path, os.path.basename(f))))
    else:
        dummy_smg = os.popen("copy %s %s" % (tmp_dir, os.path.join(output_path, os.path.basename(tmp_dir))))
    return 


def getlabelsDict(lable_path, is_handle=False):
    """
    对图像m-3-3.4.png
    return:
        {pic_0:class_0, pic_1:class_1, ...}
    """
    lable = open(lable_path)
    data = lable.readlines()
    ret = {}
    for line in data:
        # print(line[:-1].split(' ')) # ['mm', '(2).png', '10']
        tmp = line[:-1].split(' ')
        if is_handle:
            key, value = ''.join(tmp[:-1]), tmp[-1]
            if int(value) > 19:
                value = value[:-1]
        else:
            key, value = tmp
        ret[key] = value
    lable.close()
    return ret

def transformDict(label_dict):
    """
    将相同标签的图片分到一起

    return:
        type(dict) : {class_0:[pic_0, pic_1, ], class_1:[pic_0_0, pic_1_1, ]}
    """
    ret = {}
    for k,v in label_dict.items():
        if v not in ret:
            ret[v] = []
        ret[v].append(k)

    return ret


def augmentation(input_file_list, 
                output_path, 
                labels, 
                lable_output_path,
                threshed=100,
                max_gen=5,
                batch_size=1,
                save_prefix='bone',
                save_format='png', 
                ignore=False):
    """
    input_path: 待处理数据路径
    output_path: 输出路径
    labels: 待处理数据对应标签, {'pic_01.png':label_01, 'pic_02.png':label_02,...}
    lable_output_path: 重新生成的标签输出路径
    threshed: 每个年龄的最大图片数
    max_gen:单张图片扩充数
    ignore:
        True : 每张图片扩充数为max_gen
        False : 每张图片扩充数 max_gen=threshed//该年龄图片数量
    """
    print("[INFO] starting augmentation picture ")
    # files = getFiles(input_path)
    age_label = transformDict(labels)
    age_count = {}
    for k,v in age_label.items():
        age_count[k] = len(v)

    tmp_lable_container = [] # 存储标签
    start_time = datetime.datetime.now()
    total = len(input_file_list)
    tmp_dir = 'C:\\gen_pic_tmp' # 生成图片的路径
    file_dic = [] # 存储图片名字，防止重名
    fail, success, skip, count = 0, 0, 0, 0

    mkdir([output_path, lable_output_path, tmp_dir]) # 检查输出目录是否存在

    cleanDir(tmp_dir) # 清空缓存文件

    for i, f in enumerate(input_file_list):
        count += 1
        print("[INFO] %s / %s" % (count, total))
        try:
            base_name = os.path.basename(f)
            # 复制当前使用的图片至指定目录
            movePic(f, output_path)
            tmp_lable_container.append(base_name + ' ' + labels[base_name] + '\n')

            if not ignore:
                tmp_age_count = age_count[labels[base_name]]
                if tmp_age_count > threshed:
                    print("[INFO] skip, cause it beyond threshed")
                    continue 
                else:
                    max_gen = threshed // tmp_age_count
            # 载入图片
            img = loadImg(f)
            tmp_dir_sub = os.path.join(tmp_dir, str(i))
            mkdir([tmp_dir_sub])
            tmp_save_prefix = save_prefix + '_' + str(labels[base_name]) + '_' + base_name
            # 生成图片
            input_par = {
                'batch_size':batch_size, 
                'save_to_dir':tmp_dir_sub, 
                'save_prefix':tmp_save_prefix, 
                'save_format':save_format
            }
            genPic(img, max_gen=max_gen, **input_par)

            # 获得标签
            
            file_dic = getlabels(tmp_lable_container, labels[base_name], tmp_dir_sub, file_dic)
            # print(file_dic)

            # 将缓存中的图片移动到指定目录
            movePic(tmp_dir, output_path)

            # 打印信息到输出台
            printToConsole(start_time, f, count, total, 5)
            success += 1
        except Exception as e:
            # 错误情况
            saveError(e, output_path, f)
            fail += 1

    # 打乱标签列表写标签
    random.shuffle(tmp_lable_container)
    with open(os.path.join(lable_output_path, 'labels.txt'), 'w') as lable_file:
        for line in tmp_lable_container:
            lable_file.write(line)


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" % (total, success, skip, fail, expend))
    try:
        cleanDir(tmp_dir)
        shutil.rmtree(tmp_dir) # 删除缓存目录
    except:
        print('需要手动删除缓存目录: %s' % tmp_dir)
    os.startfile(output_path)


if __name__ == '__main__':

    lable_path = r'C:\Study\test\kaggle-bonage\train-male\train.txt'
    labels = getlabelsDict(lable_path)

    input_path =  r'C:\Study\test\kaggle-bonage\train-male'

    output_path = r'C:\Study\test\kaggle-bonage\test'
    lable_output_path = r'C:\Study\test\kaggle-bonage\test'
    files = getFiles(input_path)
    augmentation(files, 
                output_path, 
                labels, 
                lable_output_path,
                batch_size=1,
                save_prefix='bone',
                save_format='png')