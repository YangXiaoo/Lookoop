import argparse
import json
import os
import os.path as osp
import warnings
import sys

import PIL.Image
import yaml

from labelme import utils

try:
    import ctypes
except ImportError:
    print("Import error, no model name ctypes.")

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.

BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
 

#blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()
 
#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
 
#sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()

#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 

#pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()
 

#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()
 



def get_filename(dirpath):
    if not os.path.exists(dirpath):
        printRed("Direction not exits, please check it.\n")
        printRed("Existing system...\n")
        printRed("Goodbye, old brother...\n")
        sys.exit(0)

    files = []
    file_list = os.listdir(dirpath)
    for name in file_list:
        name = os.path.join(dirpath, name)
        if os.path.isdir(name):
            get_filename(name)
        file = os.path.splitext(name)
        file_suffix = file[1]
        if file_suffix == '':
            continue
        files.append(name)
    # print(files)
    return files

def get_path(json_file,out_dir):
    file = os.path.splitext(json_file)
    file_suffix = file[1]
    if file_suffix != '.json':
        return False
    file_name = file[0]
    file_name = file_name.split('\\')[-1]
    file_name = file_name.replace('-','_')
    dirname = os.path.join(out_dir, file_name)
    try:
        os.mkdir(dirname)
    except Exception,e:
        printRed("Something wrrong, maybe there was already file exists.\n")
        printGreen("But the system can continue to process it.")
        printRed("Error infomation: %s\n" % e)
    return dirname


def handle_json(json_file, out_dir):
    data = json.load(open(json_file))
    img = utils.img_b64_to_arr(data['imageData'])
    label_name_to_value = {'_background_': 0}
    for shape in data['shapes']:
        label_name = shape['label']
        if label_name in label_name_to_value:
            label_value = label_name_to_value[label_name]
        else:
            label_value = len(label_name_to_value)
            label_name_to_value[label_name] = label_value

    # label_values must be dense
    label_values, label_names = [], []
    for ln, lv in sorted(label_name_to_value.items(), key=lambda x: x[1]):
        label_values.append(lv)
        label_names.append(ln)
    assert label_values == list(range(len(label_values)))

    lbl = utils.shapes_to_label(img.shape, data['shapes'], label_name_to_value)

    captions = ['{}: {}'.format(lv, ln)
                for ln, lv in label_name_to_value.items()]
    lbl_viz = utils.draw_label(lbl, img, captions)

    PIL.Image.fromarray(img).save(osp.join(out_dir, 'img.png'))
    PIL.Image.fromarray(lbl).save(osp.join(out_dir, 'label.png'))
    PIL.Image.fromarray(lbl_viz).save(osp.join(out_dir, 'label_viz.png'))

    with open(osp.join(out_dir, 'label_names.txt'), 'w') as f:
        for lbl_name in label_names:
            f.write(lbl_name + '\n')

    # print('\n  info.yaml is being replaced by label_names.txt')
    info = dict(label_names=label_names)
    with open(osp.join(out_dir, 'info.yaml'), 'w') as f:
        yaml.safe_dump(info, f, default_flow_style=False)


def main():
    string1 = "\n\n**********Author(yangxiao)**********\n"
    string2 = "Hello, old brother(sister)! It is easy to use.\n\n\n"
    # color_print(string1,color='green') 
    printGreen(string1)
    printYellow(string2)
    dirpath = raw_input("Please input direction of files:")
    out_dir = raw_input("Please input save direction(default path is direction of files):")
    is_active = raw_input("Enter to process.")
    is_active = is_active.strip()
    if is_active == '':
        out_dir = out_dir.strip()
        dirpath = dirpath.strip()
    else:
        printRed("\nError command, googbye old brother!\n")  
        sys.exit(0) 

    file_list = get_filename(dirpath)
    print(file_list)
    sys.exit(0)

    total = len(file_list)
    printSkyBlue("\nTotal files %s.\n" % total)
    printRed("Do not do anything, it is processing....\n\n")
   
    
    if out_dir is '':
        out_dir = dirpath
    if not osp.exists(out_dir):
        try:
            os.mkdir(out_dir)
        except Exception:
            printRed("Old brother, please go heart, file-out direction can not create, please check your inputs.\n")
            printRed("Existing system...\n")
            printRed("Goodbye, old brother...\n")
            sys.exit(0)
    
    count = 0
    fail = 0
    for json_file in file_list:
        count += 1
        out_dir_back = out_dir
        out_dir = get_path(json_file, out_dir)
        if not out_dir:
            printRed("\nSkip a file, because the file is not JSON format.\n")
            fail += 1
            count -= 1
            continue
        handle_json(json_file, out_dir)
        out_dir = out_dir_back
        printSkyBlue("%s  compiled.\n" % json_file)

    printYellow("\n\n%s files compiled.\n" % count)
    printRed("%s files fail.\n" % fail)
    printYellow("Results show in  %s \n"  % out_dir)
    printGreen("\n\nGoodbye, old brother......")
    os.startfile(out_dir)


if __name__ == '__main__':
    main()
