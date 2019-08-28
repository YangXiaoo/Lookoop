> ## Linux

## Linux文件和目录操作
## 创建文件, 查看文件
## 创建目录
## 监测程序
## ps和top的区别
## 压缩数据
## 结束进程
## 压力测试衡量CPU的三个指标? 
CPU Utilization、Load Average和ContextSwitch Rate
## Linux下查看80端口是否被占用
`ps -ef | grep 80`
`netstat -an | grep : 80`
## 查看内存 
`free`
## 查看磁盘
`df -h` 显示已经挂载的分区列表
## 创建一个新用户
`useradd username`
## 文件权限
`chmod 777 file` 对file文件的拥有者, 同组, 其他用户都有写、读和执行权
r: 4   w: 2   x: 1
## 备份
`dump`

## 你知道库函数和内核调用吗?  
系统调用运行在内核态
库函数调用运行的用户态, 一般会通过缓冲等机制减少系统调用次数