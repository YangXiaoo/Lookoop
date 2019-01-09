#coding:utf-8
import os
import sys

def get_filename(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
    return file

def dele_space(file):
    count = 0
    for f in file:
        f_old = f
        # f_new = f
        # print(f)
        f_new = f.replace(' ','')
        f_new = f_new.replace('(','_')
        f_new = f_new.replace(')','')
        if f_old != f_new:
            os.rename(f_old, f_new)
            count += 1
            print("Old filename: %s" % f_old)
            print("New filename: %s\n" % f_new)
    print("Successful,total %s files renamed." % count)

def main():
    dirpath = r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\row_data\train\2'
    file_list = get_filename(dirpath)
    dele_space(file_list)

if __name__=='__main__':
    main()