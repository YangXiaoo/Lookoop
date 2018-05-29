import json
import os
import os.path as osp
import warnings
import sys
import re
import shutil 
import cv2  
from skimage import io  
# pip install opencv-python
def get_filename(dirpath):
    file = []
    direction = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
        for p in dirs:
            direction.append(p)
    return file,direction

def get_path(pic_file, out_dir, dirpath):
    suffix = '.png'
    prefix = 'label_viz'
    basename = os.path.basename(pic_file)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    if file_prefix != prefix:
        return False
    file_name = os.path.splitext(pic_file)
    dir_path = file_name.split(file_prefix)[-1]
    pwd = dir_path.split(os.sep)[-1:]
    dir_name = dir_path.split(dirpath)[-1]
    dir_name = os.path.json(dir_name,out_dir)
    try:
        os.makedirs(dir_name)
    except Exception,e:
        print("%s" % e)
    return dir_name,pwd

def handle(pic,pwd,out_dir):
    out_pic = os.path.join(out_dir,str(pwd)+".png")
    img = io.imread(pic)
    img = img.astype(np.uint8)
    cv2.imwrite(out_pic,img) 

def main():
    dirpath = raw_input("Please input direction of files:\n")
    out_dir = "C:\\PIC_FILE"
    file_list,dirname_list = get_filename(dirpath)
    i = 0
    for f in file_list:
        if not get_path(f,out_dir,dirpath):
            continue
            print("error: %s" % i)
            i += 1
        else:
            dir_name,pwd = get_path(f,out_dir,dirpath)
        handle(f,pwd,dir_name)
        i =+ 1
        print("%s\n" % i )