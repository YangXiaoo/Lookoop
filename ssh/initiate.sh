#!/bin/sh
#

trap '' SIGINT #信号复原
base_dir=$(dirname $0) #dirname $0，取得当前执行的脚本文件的父目录

export LANG='zh_CN.UTF-8'
python $base_dir/paramiko.py

exit
