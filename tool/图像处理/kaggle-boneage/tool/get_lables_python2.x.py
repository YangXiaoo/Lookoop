# coding:UTF-8
# 2018-12-28
import os
import copy
try:
    import pandas as pd 
except:
    os.system("pip install pandas")
    import pandas as pd 
import random

__suffix__ = ["png"]

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix__:
                file.append(path)
    return file


def get_train_lable(pic_path, csv_path, train_male_output, 
                    train_female_output, validation_male_output,
                    validation_female_output, lables_output,
                    train_size=0.7):  
    """
    获得标签并分类
    """
    print('loading data...')
    csv_file = pd.read_csv(csv_path,header = 0,encoding= 'utf8')  
    csv_data = pd.DataFrame(csv_file)  
    rows = len(csv_data) 

    out_dirs = [train_male_output, train_female_output,
                validation_male_output, validation_female_output]
    for f in out_dirs:
        if not os.path.isdir(f):
            os.mkdir(f)

    pic_files = getFiles(pic_path)
    
    # 获得csv数据
    csv_dict = {}
    for i in range(rows):
        csv_dict[str(csv_data['id'][i])] = [str(csv_data['boneage'][i]), str(csv_data['male'][i])]

    # 处理骨龄
    male_bone_age = []
    female_bone_age = []
    for k,v in csv_dict.values():
        if v == 'True':
            if k not in male_bone_age:
                male_bone_age.append(k)
        else:
            if k not in female_bone_age:
                female_bone_age.append(k)
    male_bone_age.sort(key=lambda x : int(x))
    female_bone_age.sort(key=lambda x : int(x))
    # print(male_bone_age, female_bone_age)
    sort_male_bone_age, sort_female_bone_age = {}, {}
    for k,v in enumerate(male_bone_age):
        sort_male_bone_age[v] = str(k) 
    for k,v in enumerate(female_bone_age):
        sort_female_bone_age[v] = str(k)
    # female:109, male:130
    # print(sort_female_bone_age, sort_male_bone_age) # {'4': '0', '6': '1', '9': '2', '10': '3',...}

    # 生成标签对应实际年龄
    group = [[sort_male_bone_age, 'male_lables.txt'], [sort_female_bone_age, 'female_lables.txt']]
    for g in group:
        data, lable = g 
        lable_output = open(os.path.join(lables_output, lable), 'w')
        for k, v in data.items():
            lable_output.write(v + ' ' + k + 'month\n')
        lable_output.close()


    # 获取文件列表，打乱顺序划分训练集与验证集
    data_id = copy.copy(list(pic_files))
    total = len(data_id)
    random.shuffle(data_id)
    split_index = int(total * train_size)  # 默认 70% 作为训练集
    train_data = data_id[:split_index]
    validation_data = data_id[split_index:]

    # print("getting lables and classifing image...")
    # 简化代码
    group = [[train_male_output, train_female_output,train_data], 
             [validation_male_output, validation_female_output, validation_data]]
    # 分别对验证集与训练集进行分类并生成标签
    for g in group:
        male_output, female_output, data = g
        count = 0
        male_lables = open(os.path.join(male_output, 'train.txt'), 'w')
        female_lables = open(os.path.join(female_output, 'train.txt'), 'w')
        # 将男女图片分类
        for f in data:
            count += 1
            print(str(int(count/total * 100)),' %', ' [', '#'*int(count/total * 100), '-'* (100 - int(count/total * 100)) , ']')

            pic_basename = os.path.basename(f)
            pic_id = pic_basename.split('.')[0]
            if csv_dict[pic_id][1] == 'True':
                out_dir = os.path.join(male_output, pic_basename)
                male_lables.write(pic_basename + ' ' + sort_male_bone_age[csv_dict[pic_id][0]] + '\n')
            else:
                out_dir = os.path.join(female_output, pic_basename)
                female_lables.write(pic_basename + ' ' + sort_female_bone_age[csv_dict[pic_id][0]] + '\n')
            dummy_smg = os.popen("copy %s %s" % (f, out_dir))
            if count == 100:
                break
        male_lables.close()
        female_lables.close()


if __name__ == '__main__':
    pic_path = r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset'
    csv_path = r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset.csv'
    train_male_output = r'C:\Study\test\kaggle-bonage\train-male'
    train_female_output = r'C:\Study\test\kaggle-bonage\train-female'
    validation_male_output = r'C:\Study\test\kaggle-bonage\validation-male'
    validation_female_output = r'C:\Study\test\kaggle-bonage\validation-female'
    lables_output = r'C:\Study\test\kaggle-bonage'
    get_train_lable(pic_path, csv_path, train_male_output, 
                    train_female_output, validation_male_output,
                    validation_female_output, lables_output)