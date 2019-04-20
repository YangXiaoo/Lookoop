#!C:\ProgramData\Anaconda2
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
    # print dir_name
    try:
        os.makedirs(dir_name)
    except Exception:
        pass
    return dir_name

def handle_picture(f,s,out_dir,s_path,s_name,su,er):
    suffix = "png"
    height = 512
    width = 512
    f_img = Image.open(f)
    f_img = f_img.convert("L")
    s_img = Image.open(s)
    s_img = s_img.convert("L")
    im_f = f_img 
    data_f = im_f.getdata()
    data_f = np.matrix(data_f)
    # print data_f
    im_s = s_img 
    data_s = im_s.getdata()
    data_s = np.matrix(data_s)
    mt_f = np.array(f_img)
    # mt_f = mt_f.reshape([512,512])
    # mt_f = np.reshape(mt_f,(512,512))
    mt_s = np.array(s_img)
    # print data_s
    fail = []
    dir_name = get_path(s, out_dir, s_path)
    file_name = os.path.join(dir_name,s_name)
    try:
        data = mt_f * mt_s
        new = Image.fromarray(data)
        new.save(file_name,suffix) 
        su = su + 1
        print("OK: [ %s ]" %file_name)

    except Exception as e:
        error = str(e)+": [ "+file_name+" ]\n"
        fail.append(error)
        er = er + 1

    return fail,su,er


def initial(data,height=512,width=512):
    print("Initiating data...")
    height = height / 2
    weight = width / 2
    result = []
    datas = []
    tmp = []
    row = len(data)
    line = len(data[0])
    u_c = 0
    l_c = 0
    r_c = 0
    d_c = 0
    for r in range(0,row):
        for l in range(0,line):
            if data[r][l] != 0 & u_c == 0:
                u_x = l 
                u_y = r
                u_c = 1
                break
        if u_c == 1:
            break

    for l in range(0,line):
        for r in range(0,row):
            if data[r][l] != 0 & l_c == 0:
                l_x = l 
                l_y = r 
                l_c = 1
                break
        if l_c == 1:
            break
    for r in range(row-1,0,-1):
        for l in range(line-1,0,-1):
            if data[r][l] != 0 & d_c == 0:
                d_x = l 
                d_y = r 
                d_c = 1
                break
        if d_c == 1:
            break
    for l in range(line-1,0,-1):
        for r in range(row-1,0,-1):
            if data[r][l] != 0 & r_c == 0:
                r_x = l 
                r_y = r 
                r_c = 1
                break
        if r_c == 1:
            break
    o_y = u_y + (d_y - u_y) / 2 
    o_x = l_x + (r_x - l_x) / 2 
    y_max = o_y + height
    y_min = o_y - height
    x_max = o_x + weight
    x_min = o_x - weight
    datas.append(u_x)
    datas.append(u_y)
    datas.append(l_x)
    datas.append(l_y)
    datas.append(d_x)
    datas.append(d_y)
    datas.append(r_x)
    datas.append(r_y)
    datas.append(y_max)
    datas.append(y_min)
    datas.append(x_min)
    datas.append(x_max)
    print (datas)
    for r in range(0,row):
        for l in range(0,line):
            if r<y_max and r>=y_min and l<x_max and l>= x_min:
                datu = data[r][l]
                tmp.append(datu)
        if tmp:
            result.append(tmp)
            tmp = []
    # print result
    result = np.array(result)
    return result
            


def main():
    # f_path = raw_input("\nInput original picture direction:")
    f_path = "C:\\Users\\user\\Desktop\\11"
    # s_path = raw_input("\nInput direction:")
    s_path = "C:\\Users\\user\\Desktop\\44"
    out_dir = "C:\\Users\\user\\Desktop\\55"
    starttime = datetime.datetime.now()

    f_file_list = get_filename(f_path)
    s_file_list = get_filename(s_path)
    su = 0
    er = 0
    sk = 0
    for f in f_file_list:
        f_name = os.path.basename(f)
        a_name = f_name.split('.') [0]
        for s in s_file_list:
            s_name = os.path.basename(s)
            b_name = s_name.split('.') [0]
            if a_name == b_name:
                fail,su,er = handle_picture(f,s,out_dir,s_path,s_name,su,er)
                s_file_list.remove(s)
            else:
                print("Skip: [ %s ]" % s)
                sk = sk + 1

    endtime = datetime.datetime.now()
    expend = endtime - starttime
    """
    if fail:
        print("*****************************************************")
        print (fail)
    print("*****************************************************")
    print("Begn: [ %s ]" % starttime)
    print("Time: [ %s ]" % expend)
    print("Succ: [ %s ]" % su)
    print("Skip: [ %s ]" % sk)
    print("Erro: [ %s ]" % er)
    """
if __name__ == '__main__':
    main()
