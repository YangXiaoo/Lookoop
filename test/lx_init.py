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
try:
    from PIL import Image
except:
    os.system("pip install Pillow")
    from PIL import Image
    
def get_filename(dirpath):
    file = []
    direction = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            file.append(path)
        for p in dirs:
            direction.append(p)
    return file

def get_path(pic_file, out_dir, dirpath):
    suffix = '.png'
    prefix = 'label'
    basename = os.path.basename(pic_file)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    dirname = os.path.dirname(pic_file)
    dir_path = dirname.split(dirpath)[-1]
    dir_ = dir_path.strip('\\')
    dir_name = os.path.join(out_dir,dir_)
    print dir_name
    try:
        os.makedirs(dir_name)
    except Exception,e:
        pass
    return dir_name

def main():
    fail = []
    f_path = raw_input("\nInput original picture direction:")
    # f_path = "D:\\page\\2"
    s_path = raw_input("\nInput direction:")
    # s_path = "D:\\page\\11"
    out_dir = "C:\\HANDLE_FILE\\"
    f_file_list = get_filename(f_path)
    s_file_list = get_filename(s_path)
    sk = 0
    su = 0
    for f in f_file_list:
        f_name = os.path.basename(f)
        for s in s_file_list:
            s_name = os.path.basename(s)
            if s_name == f_name:
                f_img = Image.open(f)
                f_img = f_img.convert("L")
                s_img = Image.open(s)
                s_img = s_img.convert("L")
                im_f = f_img 
                data_f = im_f.getdata()
                data_f = np.matrix(data_f)
                print data_f
                im_s = s_img 
                data_s = im_s.getdata()
                data_s = np.matrix(data_s)
                mt_f = np.array(f_img)
                mt_s = np.array(s_img)
                print data_s
                try:
                    data = mt_f * mt_s
                    new = Image.fromarray(data)
                    dir_name = get_path(s, out_dir, s_path)
                    file_name = os.path.join(dir_name,s_name)
                    new.save(file_name,"png") 
                    su = su + 1
                except:
                    sk = sk + 1
                    print("error: [ %s ]" % file_name)
                    fail.append(file_name)
    print fail
    print("Successful: [ %s ]" % su)
    print("Fail: [ %s ]" % sk)
if __name__ == '__main__':
    main()
