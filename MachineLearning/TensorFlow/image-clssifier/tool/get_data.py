# coding:UTF-8
# 2018-12-28
# update:2019-1-3, 均等分配训练集与验证集
# update:2019-1-12, 修复由于数据集分布不均，导致验证集精确度较低

import os
import math
try:
    import pandas as pd 
except:
    os.system("pip install pandas")
    import pandas as pd 
import random

__suffix__ = ["png"]

def get_files(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix__:
                file.append(path)
    return file


def mkdir(file_list):
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 


def _split_data(age_pic, train_size, threshed=5):
    """
    age_pic: {bone_age : [pic_id, ], ...}
    train_size: range(0, 1)

    return :
        ret_train: [pic_id, ]
        ret_validation: [pic_id, ]
    """
    ret_train, ret_validation = [], []
    for k,v in age_pic.items():
        age_count = len(v)
        if int(math.floor(age_count * threshed)) < threshed:
            split = 0
        else:
            split = int(math.floor(age_count * (1- train_size)))
        ret_validation.extend(v[:split])
        ret_train.extend(v[split:])

    return ret_train, ret_validation


def _get_pic_map(pic_files):
    """
    pic_files: [pic_path, ]
    
    return: {pic_id : [file_path,]}
    """
    file_dict = {} 
    for f in pic_files:
        pic_basename = os.path.basename(f)
        pic_id = pic_basename.split('.')[0]
        file_dict[pic_id] =  f

    return file_dict


def _get_data_lables(train_output, 
                    validation_output, 
                    train_data, 
                    validation_data,
                    sort_bone_age,
                    file_dict,
                    csv_dict):
    """
    train_output: string, file path
    validation_output: string, file path
    train_data: [pic_id, ]
    validation_data: [pic_id, ]
    file_dict: {pic_id : [file_path]}
    csv_dict: {pic_id:[boneage, male]}

    return: None
    """
    print("getting data...")
    train_files = []
    train_labels = []
    validation_files = []
    validation_labels = []
    group = [[train_output, train_data, train_files, train_labels, 'labels.txt'],
            [validation_output, validation_data, validation_files, validation_labels, 'labels.txt']]

    for g in group:
        output, data, files, labels, label_txt = g 
        # labels = open(os.path.join(output, label_txt), 'w')
        for pic_id in data:
            f = file_dict[pic_id]
            pic_basename = os.path.basename(f)
            out_dir = os.path.join(output, pic_basename)
            tmp_label = pic_basename + ' ' + sort_bone_age[csv_dict[pic_id][0]] + '\n'
            files.append([f, out_dir])
            labels.append(tmp_label)
            # labels.write(tmp_label)
            # dummy_smg = os.popen("copy %s %s" % (f, out_dir))
        # labels.close()

    return [[train_output, train_files, train_labels], [validation_output, validation_files, validation_labels]]

def _write_result(result):
    """
    将数据标签写入文件
    移动图片至输出路径
    Args:
        result: [[train_output, train_files, train_labels], [validation_output, validation_files, validation_labels]]

        return : None
    """
    for g in result:
        output, files, labels = g 
        with open(os.path.join(output, 'labels.txt'), 'w') as f:
            for line in labels:
                f.write(line)

        for f,out_dir in files:
            dummy_smg = os.popen("copy %s %s" % (f, out_dir))




def main(pic_path,
        csv_path,
        train_male_output, 
        train_female_output,
        validation_male_output,
        validation_female_output,
        lables_output,
        train_size=0.7,
        threshed=5, 
        is_wirte=True):   
    """
    获得标签并分类
    """

    print('loading data...')
    csv_file = pd.read_csv(csv_path,header = 0,encoding= 'utf8')  
    csv_data = pd.DataFrame(csv_file)  
    rows = len(csv_data) 

    mkdir([train_male_output, 
            train_female_output,
            validation_male_output, 
            validation_female_output])

    pic_files = get_files(pic_path)
    
    # 获得csv数据
    csv_dict = {} # {pic_id:[boneage, male]}
    male_age_pic = {} # {bone_age:[pic_id, ]}
    female_age_pic = {}
    for i in range(rows):
        pic_id = str(csv_data['id'][i])
        bone_age = str(csv_data['boneage'][i])
        is_male = str(csv_data['male'][i])
        csv_dict[pic_id] = [bone_age, is_male]
        if is_male == 'True':
            if bone_age not in male_age_pic:
                male_age_pic[bone_age] = []
            male_age_pic[bone_age].append(pic_id)
        else:
            if bone_age not in female_age_pic:
                female_age_pic[bone_age] = []
            female_age_pic[bone_age].append(pic_id)

    # 对年龄进行分类
    male_bone_age = sorted(male_age_pic.keys(), key=lambda x:int(x))
    female_bone_age = sorted(female_age_pic.keys(), key=lambda x:int(x))
    sort_male_bone_age, sort_female_bone_age = {}, {} # {true_age:rename_class}
    for k,v in enumerate(male_bone_age):
        sort_male_bone_age[v] = str(k) 
    for k,v in enumerate(female_bone_age):
        sort_female_bone_age[v] = str(k)
    # female:109, male:130
    # print(sort_female_bone_age, sort_male_bone_age) # {'4': '0', '6': '1', '9': '2', '10': '3',...}

    # 生成标签对应实际年龄
    group = [[sort_male_bone_age, 'male_lables.txt'], 
            [sort_female_bone_age, 'female_lables.txt']]
    for g in group:
        data, lable = g 
        lable_output = open(os.path.join(lables_output, lable), 'w')
        for k, v in data.items():
            lable_output.write(v + ' ' + k + '\n') # format: `class actual_age`
        lable_output.close()


    # 获取文件列表，打乱顺序划分训练集与验证集
    male_train, male_validation = _split_data(male_age_pic, train_size, threshed)
    # print(len(male_train))
    female_train, female_validation = _split_data(female_age_pic, train_size, threshed)

    # 获得pic_id到路径的映射
    file_dict = _get_pic_map(pic_files)


    # male
    print("male...")
    ret_1 = _get_data_lables(train_male_output, 
                    validation_male_output, 
                    male_train, 
                    male_validation,
                    sort_male_bone_age,
                    file_dict,
                    csv_dict)

    # female
    print("female...")
    ret_2 = _get_data_lables(train_female_output, 
                    validation_female_output, 
                    female_train, 
                    female_validation,
                    sort_female_bone_age,
                    file_dict,
                    csv_dict)
    if is_wirte:
        _write_result(ret_1)
        _write_result(ret_2)
    os.startfile(train_male_output)


if __name__ == '__main__':
    pic_path = r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset'
    csv_path = r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset.csv'
    train_male_output = r'C:\Study\test\kaggle-bonage\train-male'
    train_female_output = r'C:\Study\test\kaggle-bonage\train-female'
    validation_male_output = r'C:\Study\test\kaggle-bonage\validation-male'
    validation_female_output = r'C:\Study\test\kaggle-bonage\validation-female'
    lables_output = r'C:\Study\test\kaggle-bonage'

    main(pic_path, 
        csv_path, 
        train_male_output,
        train_female_output, 
        validation_male_output,
        validation_female_output, 
        lables_output)