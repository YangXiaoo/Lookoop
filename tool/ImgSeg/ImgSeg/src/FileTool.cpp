// FileTool.cc
// 2019-2-25
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <direct.h> // mkdir()
#include <io.h> // _access()
#include <iterator>

#include "../include/FileTool.hpp"


using namespace std;

/* 文件是否存在 */
bool file_exist(const string &file_path) {
    // ifstream f(file_path.c_str());
    // return f.good();
	fstream _file;
	_file.open(file_path, ios::in);
	if (!_file) {
		return false;
	}
	return true;
}


/* 文件夹是否存在 */
bool folder_exist(string &folder_path) {
	// char *folder = folder_path.c_str();
	if (_access(folder_path.c_str(), 0) == -1) {
		return false;
	}
	return true;
}


/* 创建文件夹 */
int mkdirs(string &folder_path) {
	int folder_create = 0;
	for (auto it = folder_path.begin(); it != folder_path.end(); ++it) {
		if (*it == '\\' || *it == '/') {
			string cur_path(folder_path.begin(), it);
			if (_access(cur_path.c_str(), 0) == -1) {
				_mkdir(cur_path.c_str());
				++folder_create;	
			}

		}
	}
	string cur_path(folder_path.begin(), folder_path.end());
	if (_access(cur_path.c_str(), 0) == -1) {
		_mkdir(cur_path.c_str());
		++folder_create;	
	}

	return folder_create;
}


/* 替换字符串中指定字符串 */
void str_replace(string &str, const string &old_smb, const string &new_smb) {
	// cout << "[INFO] str_replace()" << endl;
	string::size_type pos = 0;
	string::size_type old_len = old_smb.size();
	string::size_type new_len = new_smb.size();
	while ((pos = str.find(old_smb, pos)) != string::npos) {
		str.replace(pos, old_len, new_smb);
		pos += new_len;
	}
}


/* 连接路径 */
string path_join(string pre_path, string suf_path) {
	// cout << "[INFO] call path_join()" << endl;
	string joined_path;
	string backslash = {"\\"};
	string slash = {"/"}; // 为了Linux上能用, 统一分隔符
	str_replace(pre_path, backslash, slash);
	str_replace(suf_path, backslash, slash);

	// string last_str(pre_path.back());
	if (pre_path.back() != '/')
		pre_path += slash;

	// string fst_str(suf_path.front());
	if (suf_path.front() == '/')
		suf_path.erase(suf_path.begin());

	joined_path = pre_path + suf_path;

	return joined_path;
}


/* 文件名 */
string path_basename(const string &path) {
	string slash = {"/"}, backslash = {"\\"};
	string::size_type pos;
	// string::size_type end = path.size();
	pos = path.rfind(slash);
	if (pos == string::npos)
		pos = path.rfind(backslash);
	string file_name(path.substr(++pos));
	// cout << "[INFO] file basename: " << file_name << endl;

	return file_name;
}


/* 文件名分开 */
vector<string> path_splitext(const string &path) {
	string split_smb = {"."};
	string::size_type pos;
	string::size_type end = path.size();
	pos = path.rfind(split_smb);
	vector<string> file;
	file.push_back(path.substr(0, pos));
	file.push_back(path.substr(pos, end));

	return file;
}

/* 文件所在目录路径 */
string path_dirpath(const string &path) {
	string slash = {"/"}, backslash = {"\\"};
	string::size_type pos;
	// string::size_type end = path.size();
	pos = path.rfind(slash);
	if (pos == string::npos)
		pos = path.rfind(backslash);
	string dir_path(path.substr(0, pos));

	return dir_path;
}

/*********************** class-Files ***********************/

/** 
 * 构造函数
 * @param dir : 待遍历路径
 * @param patt : 文件名后缀, std::vector<string> patt{"*.png", "*.jpg"};
 * @param model : 文件路径模式, 默认读取完整路径
 * @return 根据参数初始化读取文件类型
 */
// Files::Files(std::string dir, 
//              std::vector<string> patt, 
//              int model) {
//     _model_choose(model)
// }


void Files::_model_choose(int model) {
    switch (model) {
        case 0 : read_model = FULL_PATH; break;
        case 1 : read_model = FILE_NAME; break;
        case 2 : read_model = CUR_FILE; break;
        case 3 : read_model = CUR_DIR; break;
    }
}


const int Files::s_default_read_model = 0; // 默认读取文件模式


/** 
 * 直接对外接口
 * @param files_list : 空vector<string>
 * @output &files_list : 返回遍历后的容器
 */
void Files::get_files(vector<string> &files_list) {
	// Model[read_model]指向一个读取模式成员函数
    (this->*s_Model[read_model])(dir_path, files_list);
}


/* 重载 */
void Files::get_files(vector<string> &files_list, vector<string> patt) {
    filter_patt = patt;
    // Model[read_model]指向一个读取模式成员函数
    (this->*s_Model[read_model])(dir_path, files_list);
}


/* 重载 */
void Files::get_files(vector<string> &files_list, int model) {
    _model_choose(model);
    // Model[read_model]指向一个读取模式成员函数
    (this->*s_Model[read_model])(dir_path, files_list);
}


/* 重载 */
void Files::get_files(vector<string> &files_list, 
					  vector<string> patt,
					  int model) {
    filter_patt = patt;
    _model_choose(model);
    // Model[read_model]指向一个读取模式成员函数
    (this->*s_Model[read_model])(dir_path, files_list);
}


/* 文件格式是否匹配 */
template <typename file_t>
bool Files::_patt_in_name(file_t &file_info) {
	bool flag = false;
    if (!filter_patt.empty()) {
        for (const auto it : filter_patt) {
            if (!it.empty()){
                string cur_file_name(begin(file_info.name), end(file_info.name));
                string::size_type pos = cur_file_name.find(it);
                if (pos != string::npos)
                    flag = true;
            }
        }
		if (!flag)
			return false;
    } 
    return true;
}



// 获取指定文件夹下所有指定格式文件的全路径
void Files::get_full_path(string path, vector<string> &files_list) {

	// typedef long int intptr_t; 
	intptr_t file_handle = 0;
    _finddata_t file_info;  // 文件信息读取结构
    string p; 

    // long _findfirst(const char *, struct _finddata_t *);
    if ((file_handle = _findfirst(p.assign(path).append("\\*").c_str(), &file_info)) != -1) { 
        /* 若存在子文件夹 */
        do {
            if ((file_info.attrib & _A_SUBDIR)) {  //比较文件类型是否是文件夹
                if (strcmp(file_info.name, ".") != 0 
                    && strcmp(file_info.name, "..") != 0) {
                    get_full_path(p.assign(path).append("\\").append(file_info.name), files_list);
                }
            }
            else { // 若不是文件夹则为文件，判断后缀
                if (_patt_in_name(file_info))
                    files_list.push_back(p.assign(path).append("\\").append(file_info.name));
            }
        } while (_findnext(file_handle, &file_info) == 0);  //寻找下一个，成功返回0，否则-1
        _findclose(file_handle);  
    }
}



/* 获取指定文件夹下所有指定格式文件名的全路径 */
void Files::get_file_name(string path, vector<string> &files_list) {
	// typedef long int intptr_t;
	intptr_t file_handle = 0;
    _finddata_t file_info;  // 文件信息读取结构
    string p; 

    // long _findfirst(const char *, struct _finddata_t *);
    if ((file_handle = _findfirst(p.assign(path).append("\\*").c_str(), &file_info)) != -1) { 
        /* 若存在子文件夹 */
        do {
            if ((file_info.attrib & _A_SUBDIR)) {  //比较文件类型是否是文件夹
                if (strcmp(file_info.name, ".") != 0 
                    && strcmp(file_info.name, "..") != 0) {
                    get_file_name(p.assign(path).append("\\").append(file_info.name), files_list);
                }
            }
            else { // 若不是文件夹则为文件，判断后缀
                if (_patt_in_name(file_info))
                    files_list.emplace_back(file_info.name);
            }
        } while (_findnext(file_handle, &file_info) == 0);  //寻找下一个，成功返回0，否则-1
        _findclose(file_handle);  
    }
}


/* 获取指定文件夹下的所有当前文件夹名称, 深度为1 */
void Files::get_cur_file(string path, vector<string> &files_list) {
	// typedef long int intptr_t;
	intptr_t file_handle = 0;
    _finddata_t file_info;
    string p; 
    if ((file_handle = _findfirst(p.assign(path).append("\\*").c_str(), &file_info)) != -1) {
        do {
            if (!(file_info.attrib & _A_SUBDIR)) {
                if (_patt_in_name(file_info))
                    files_list.push_back(p.assign(path).append("\\").append(file_info.name));
            }
        } while (_findnext(file_handle, &file_info) == 0);
        _findclose(file_handle);
    }
}


/* 获取指定文件夹下的所有当前文件名, 深度为1 */
void Files::get_cur_dir(string path, vector<string> &files_list) {
	// typedef long int intptr_t;
	intptr_t file_handle = 0;
    _finddata_t file_info;
    string p; 
    if ((file_handle = _findfirst(p.assign(path).append("\\*").c_str(), &file_info)) != -1) {
        do {
            if (file_info.attrib & _A_SUBDIR) {
                if (strcmp(file_info.name, ".") != 0 
                    && strcmp(file_info.name, "..") != 0) {
                    if (_patt_in_name(file_info))
                        files_list.push_back(p.assign(path).append("\\").append(file_info.name));
                }
            }
        } while (_findnext(file_handle, &file_info) == 0);
        _findclose(file_handle);
    }
}


// 初始化格式表
Files::Model Files::s_Model[] = { &Files::get_full_path,
                                  &Files::get_file_name,
                                  &Files::get_cur_file,
                                  &Files::get_cur_dir};