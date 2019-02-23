// 2019-2-22
#ifndef FILES_H
#define FILES_H

#include <vector>
#include <string>
#include <io.h>
using namespace std;

class Files {
 public:
	using Model = void (Files::*)(std::string, std::vector<string>&);	// 指向一种文件读取方法的指针

	Files() = default;
	Files(std::string dir,
		  std::vector<string> patt = std::vector<string>{},
		  int model = s_default_read_model)
		  : dir_path(dir), filter_patt(patt), read_model(FULL_PATH) { _model_choose(model); };
	Files(const Files&) = delete; 				// 复制构造函数
	Files &operator=(const string&) = delete; 	// 赋值构造函数

	// ~Files() noexcept;

	void _model_choose(int model);
	void get_files(std::vector<string> &files_list,
				   				  std::vector<string> patt = std::vector<string>(),
				   				  int model = s_default_read_model);

 private:
	enum { FULL_PATH, 		// 完整文件路径
		   FILE_NAME, 		// 只获取文件名
		   CUR_FILE, 		// 当前文件夹下的文件名
		   CUR_DIR,		// 当前文件夹下的文件夹名
		 } read_model;

	std::string dir_path; 				// 待读取路径
	std::vector<string> filter_patt; 	// 过滤模式

	static const int s_default_read_model;

 public:
	template <typename file_t> bool _patt_in_name(file_t &file_info);
	// bool _patt_in_name(struct _finddata_t);
	// 获取指定文件夹下所有指定格式文件的全路径
	void get_full_path(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下所有指定格式文件名的全路径	
	void get_file_name(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下的所有当前文件名, 深度为1	
	void get_cur_file(std::string path, std::vector<string> &files_list);
	// 获取指定文件夹下的所有当前文件夹名称, 深度为1	
	void get_cur_dir(std::string path, std::vector<string> &files_list);



 private:
	static Model s_Model[];	// 定义一个格式表，存储不同方式的读取函数

};

#endif