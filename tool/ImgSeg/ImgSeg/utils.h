// utils.h
// 常用工具

#include <vector>
#include <string>


#ifndef UTILS
#define UTILS

/* 生成序列 */
void gen_range(std::vector<int> &container, int low, 
			   int high, int gap, int max_gen);


/* 数据读取 */
class Data {
 public:
 	Data() = default;
 	Data(const std::string &path) : _path(path) { _check(); };
 	// 读取数据
 	template <typename data_type> 
 	void get_data();

 private:
 	// 检查文件是否存在
 	void _check()
 	// 待读取文件路径
 	std::string _path;
}

#endif // UTILS
