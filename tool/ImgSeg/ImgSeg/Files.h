// 2019-2-22
#ifndef FILES_H
#define FILES_H

#include <vector>
#include <string>
using namespace std;

class Files {
 public:
	using Format = std::vector<string> &(Files::*)();	// 指向一种文件读取方法的指针

	Files() = default;
	Files(std::string dir, 
		  std::vector<string> patt = std::vector<string> {}, 
		  int format = s_default_read_model)
		: dir_path(dir), filter_patt(patt) {}
	// Files(const Files&); 				// 复制构造函数
	// Files &operator=(const string&); 	// 赋值构造函数

	~Files() noexcept;

	void get_files(std::vector<string> &files_list);

 private:
	typedef enum : int {
		FULL_PATH, 		// 完整文件路径
		FILE_NAME, 		// 只获取文件名
		CUR_FILE, 		// 当前文件夹下的文件名
		CUR_DIR,		// 当前文件夹下的文件夹名
	} Read_Model;

	std::string dir_path; 				// 待读取路径
	std::vector<string> filter_patt; 	// 过滤模式
	Read_Model read_model;			// 文件读取模式

	static const int s_default_read_model;

 public:
	bool _patt_in_name(template <typename file_t> file_t &file_info);

 	// 获取指定文件夹下所有指定格式文件的全路径
	std::vector<string> get_full_path(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下所有指定格式文件名的全路径	
	std::vector<string> get_file_name(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下的所有当前文件名, 深度为1	
	std::vector<string> get_cur_file(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下的所有当前文件夹名称, 深度为1	
	std::vector<string> get_cur_dir(std::string path, std::vector<string> &files_list);	



 private:
	static Format s_Model[];	// 定义一个格式表，存储不同方式的读取函数
};

#endif