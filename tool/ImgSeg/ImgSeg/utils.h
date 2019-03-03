// utils.h
// 常用工具

#include <vector>
#include <string>
#include <map>
#include <functional>

// OpenCV
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

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
 	std::vector<std::vector<std::string>> get_data(int col_base=_base);
	void get_data(std::vector<std::vector<std::string>> &container, int col_base = _base);
	// 根据索引划分数据
	void get_data(std::vector<std::vector<std::string>> &left_data, 
				  std::vector<std::vector<std::string>> &right_data, 
				  int split, int col_base = _base);
	// 检查文件是否存在
	void _check();
 private:
 	// 待读取文件路径
 	std::string _path;
 	static const int _base = 0;
};


/* 数据转换 */
class Trans: public Data {
 public:
 	Trans() = default;
 	// 继承父类构造
 	Trans(const std::string &path) : Data(path) {};
	Trans(const std::vector<std::vector<std::string>> &data) : _p_data(data) {};
	// 转换为指定格式
	template <typename _tran_type>
	void convert_to(_tran_type &new_data);
	// 转换为矩阵<float>类型
	void convert_to_mat(Mat &new_data);
	void _get_data();
 private:
 	std::vector<std::vector<std::string>> _p_data;
};



/* 获得数据 */
void get_train_data(const std::string &file_path, Mat &feature, 
					Mat &labels, int col_base=0);
#endif // UTILS
