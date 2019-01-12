# coding:UTF-8
# 2019-1-9
# k-fold 处理数据
# 将kaggle-boneage相同年龄图片整理到一个文件夹下以便TF数据转换


import os

_suffix = ["png"]

def getFiles(dirpath):
    """
    获取文件
    """
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in _suffix:
                file.append(path)
    return file


def getLabelsDict(lable_path):
    lable = open(lable_path)
    data = lable.readlines()
    ret = {}
    for line in data:
        tmp = line[:-1].split(' ')
        key, value = ''.join(tmp[:-1]), tmp[-1]
        ret[key] = value
    lable.close()
    return ret


def mkdir(file_list):
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 


def transformDict(label_dict):
    """
    将相同标签的图片分到一起
    """
    ret = {}
    for k,v in label_dict.items():
        if v not in ret:
            ret[v] = []
        ret[v].append(k)

    return ret


def disposal(input_dir, output_dir, labels_dict, k_fold=5):
    """
    labels_dict: get by `getLabelsDict`
    """
    files = getFiles(input_dir)
    mkdir(output_dir)

    tans_label_dict = transformDict(labels_dict)
    # print(tans_label_dict)

    k_list = []
    for i in range(k_fold):
        tmp_list = {}
        for k,v in tans_label_dict.items():
            tmp_data = {}
            tmp_class_len = len(v)
            split = tmp_class_len // k_fold
            start = i * split
            last =  (i + 1) * split if i != (k_fold - 1)  else tmp_class_len
            for j in v[start : last]:
                tmp_data[j] = k 
            tmp_list = dict(tmp_list, **tmp_data)
        k_list.append(tmp_list)

    # print(k_list)
    # print(len(k_list))
    # print(len(k_list[0]), len(k_list[1]), len(k_list[-1]))
    # print(k_list[0])

    # k-fold:将其中一个作为test其余作为train
    for index,data in enumerate(k_list):
        tmp_k_dir = os.path.join(output_dir, str(index))
        k_train = os.path.join(tmp_k_dir, 'train')
        k_test = os.path.join(tmp_k_dir, 'test')
        print('generate dataset: %s' % index)
        mkdir([tmp_k_dir, k_train, k_test])
        
        for k_index,k_data in enumerate(k_list):

            if k_index == index: # test
                tmp_dir = {}
                for count,f in enumerate(files):
                    base_name = os.path.basename(f)
                    if base_name not in k_data:
                        continue
                    class_label = k_data[base_name]
                    if class_label not in tmp_dir:
                        tmp_class_dir = os.path.join(k_test, class_label)
                        mkdir(tmp_class_dir)
                        tmp_dir[class_label] = tmp_class_dir
                    tmp_class_dir = tmp_dir[class_label]

                    dummy_msg = os.popen("copy %s %s" % (f, os.path.join(tmp_class_dir, base_name)))
            else:
                tmp_dir = {}
                for count,f in enumerate(files):
                    base_name = os.path.basename(f)
                    if base_name not in k_data:
                        continue
                    class_label = k_data[base_name]
                    if class_label not in tmp_dir:
                        tmp_class_dir = os.path.join(k_train, class_label)
                        mkdir(tmp_class_dir)
                        tmp_dir[class_label] = tmp_class_dir
                    tmp_class_dir = tmp_dir[class_label]

                    dummy_msg = os.popen("copy %s %s" % (f, os.path.join(tmp_class_dir, base_name)))

    os.startfile(output_dir)


if __name__ == '__main__':
    input_dir = r'C:\Study\test\kaggle-bonage\train-male'
    output_dir = r'C:\Study\test\kaggle-bonage\train-male_disposal_out'
    lable_path = r'C:\Study\test\kaggle-bonage\train-male\train.txt'
    labels_dict = getLabelsDict(lable_path)
    disposal(input_dir, output_dir, labels_dict)


