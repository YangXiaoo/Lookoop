# coding:UTF-8
# 2018-10-17

def getData(file_path, new_file, out_file):
    '''
    导入训练数据
    file_path: 标签文件
    new_file: 数据文件
    将数据合成保存到out_file文件中
    '''
    # 获得数据标签   
    f = open(file_path)
    feature = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        for i in range(len(lines)):
            feature_tmp.append(lines[i])
        feature.append(feature_tmp)
    f.close()

    # 将标签添加到数据中
    new_f = open(new_file)
    new_feature = []
    label = []
    row = 0
    for line in new_f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        # print(row, float(feature[row][0]), float(lines[0]))
        if  row < len(feature) and float(feature[row][0]) == float(lines[0]):
            for i in range(len(lines) - 1):
                feature_tmp.append(lines[i])
            new_feature.append(feature_tmp)
            label.append(feature[row][-1])
            row += 1
    new_f.close()

    n_f = open(out_file, "w")
    m = len(new_feature)
    for i in range(m):
        n_f.write("\t".join(new_feature[i]) + '\t' + str(label[i]) + '\n')

    n_f.close()


if __name__ == '__main__':
    label = "C:\\Study\\test\\data\\label.txt"
    data = "C:\\Study\\test\\data\\data.txt"
    new_data = "new_.txt"
    getData(label, data, new_data)