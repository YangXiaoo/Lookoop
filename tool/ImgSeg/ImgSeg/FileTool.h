// FileTool.h
// 2019-2-25
#ifndef FILEE_TOOL
#define FILEE_TOOL 

#include <string>
#include <vector>
#include <string>


/* 文件是否存在 */
inline bool file_exist(const std::string &file_path);


/* 文件夹是否存在 */
inline bool folder_exist(const std::string &folder_path);


/* 创建文件夹 */
inline int mkdirs(const std::string &folder_path);


/* 替换字符串中指定字符串 */
inline void str_replace(std::string &str, 
						std::string &old_smb, 
						std::string &new_smb);


/* 连接路径 */
inline std::string path_join(std::string pre_path, std::string suf_path);


/* 文件名 */
inline std::string path_basename(const std::string path);


/* 文件后缀 */
inline std::vector<string> path_splitxt(const std::string path);


/* 读取文件路径 */
class Files {
 public:
	using Model = void (Files::*)(std::string, std::vector<string>&);	// 指向一种文件读取方法的指针

	Files() = default;
	Files(std::string dir) : dir_path(dir), filter_patt(patt), read_model(FULL_PATH) { }
	Files(std::string dir, std::vector<string> patt = std::vector<string>{})
		  : dir_path(dir), filter_patt(patt), read_model(FULL_PATH) { }
	Files(std::string dir,
	  	  std::vector<string> patt = std::vector<string>{},
	  	  int model = s_default_read_model)
	  	  : dir_path(dir), filter_patt(patt), read_model(FULL_PATH) { _model_choose(model); };
	Files(const Files&) = delete; 				// 复制构造函数
	Files &operator=(const string&) = delete; 	// 赋值构造函数

	// ~Files() noexcept;

	void _model_choose(int model);
	void get_files(std::vector<string> &files_list);
	void get_files(std::vector<string> &files_list,
				   std::vector<string> patt = std::vector<string>());
	void get_files(std::vector<string> &files_list, int model);
	void get_files(std::vector<string> &files_list,
				   std::vector<string> patt = std::vector<string>(),
				   int model);

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