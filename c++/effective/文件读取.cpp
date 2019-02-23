struct _finddata_t {
unsigned attrib;
time_t time_create; 
time_t time_access; 
time_t time_write;
_fsize_t size;
char name[260];
};

time_t，其实就是long
而_fsize_t，就是unsigned long

attrib，就是所查找文件的属性：_A_ARCH（存档）、_A_HIDDEN（隐藏）、_A_NORMAL（正常）、_A_RDONLY（只读）、 _A_SUBDIR（文件夹）、_A_SYSTEM（系统）当一个文件有多个属性时，它往往是通过位或的方式，来得到几个属性的综合。例如只读+隐藏+系统属性，应该为：_A_HIDDEN | _A_RDONLY | _A_SYSTEM 。

time_create、time_access和time_write分别是创建文件的时间、最后一次访问文件的时间和文件最后被修改的时间。

size：文件大小

name：文件名。


三、用 _findfirst 和 _findnext 查找文件

1、_findfirst函数：long _findfirst(const char *, struct _finddata_t *);

第一个参数为文件名，可以用"*.*"来查找所有文件，也可以用"*.cpp"来查找.cpp文件。第二个参数是_finddata_t结构体指针。若查找成功，返回文件句柄，若失败，返回-1。


2、_findnext函数：int _findnext(long, struct _finddata_t *);

第一个参数为文件句柄，第二个参数同样为_finddata_t结构体指针。若查找成功，返回0，失败返回-1。

3、_findclose()函数：int _findclose(long);

只有一个参数，文件句柄。若关闭成功返回0，失败返回-1。
