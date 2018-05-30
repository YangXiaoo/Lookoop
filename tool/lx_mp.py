import os
import sys 
import datetime
import time
# pip install opencv-python
# pip install scikit-image
# pip install numpy
try:
    import cv2 
except:
    os.system("pip install opencv-python")
    import cv2

try:
    from skimage import io  
except:
    os.system("pip install scikit-image")
    from skimage import io
try:
    import numpy as np
except:
    os.system("pip install numpy")
    import numpy as np

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
    prefix = 'label'
    basename = os.path.basename(pic_file)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    if file_prefix != prefix:
        print("Skip: %s " % pic_file)
        return False
    else:
        print("Move %s" % pic_file)
    dirname = os.path.dirname(pic_file)
    file_name = os.path.splitext(pic_file)
    # print file_name
    pwd = dirname.split(os.sep)[-1]
    # print("pwd: %s" % pwd)
    dir_path = dirname.split(pwd)[0]
    # print dir_path
    dir_name = dir_path.split(dirpath)[-1]
    dir_name = dir_name.strip('\\')
    # print dir_name
    dir_name = os.path.join(out_dir,dir_name)
    # print dir_name
    try:
        os.makedirs(dir_name)
    except Exception,e:
        pass
        # print("%s" % e)
    return dir_name,pwd

def handle(pic,pwd,out_dir):
    out_pic = os.path.join(out_dir,str(pwd)+".png")
    img = io.imread(pic)
    img = img.astype(np.uint8)
    cv2.imwrite(out_pic,img)
    print("Saved in %s" % out_pic) 

def main():
    print("************************")
    print("*     LiuXinXinXin~    *")
    print("*       2018-5-29      *")
    print("************************")
    dirpath = raw_input("\nInput direction:")
    starttime = datetime.datetime.now()
    # dirpath = "C:\\JSON_FILE"
    out_dir = "C:\\PIC_FILE\\"
    file_list,dirname_list = get_filename(dirpath)
    i = 0
    for f in file_list:
        if not get_path(f,out_dir,dirpath):
            continue
            print("Error:[ %s ]" % f)
            i = i + 1
        else:
            dir_name,pwd = get_path(f,out_dir,dirpath)
        i = i + 1
        handle(f,pwd,dir_name)
    endtime = datetime.datetime.now()
    expend = endtime - starttime
    print("\n**************************")
    print("Total: [ %s ]" % i )
    print("Time: [ %s ]" % expend)
main()
