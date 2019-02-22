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