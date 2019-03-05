// utils.cc
// 常用工具
#include <vector>
#include <string>

#include <fstream>
#include <iostream>
#include <sstream>
// OpenCV
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

#include "../include/utils.hpp"
#include "../include/FileTool.hpp"

using namespace std;

/* 生成序列 */
void gen_range(vector<int> &container, int low, int high, int gap, int max_gen) {
    int gen_counter = 0;
    while (low < high && gen_counter < max_gen) {
        if (gap > 0) {
            container.push_back(low);
            low += gap;
        } else {
            container.push_back(high);
            high += gap;
        }
        gen_counter += 1;

    } 
}


/*********************** Data 数据读取 ***********************/
// 检查文件是否存在
void Data::_check() {
    if (!file_exist(_path)) {
        cout << "[WARNING] file does not exit: " << _path << endl;
    }
}


// 读取数据
vector<vector<string>> Data::get_data(int col_base) {
    vector<vector<string>> container;
    ifstream data_in;
    data_in.open(_path, ios::in);
    if (!data_in.is_open()) {
        cout << "open File Failed." << endl;
        return container;
    }

    string line;
    // 输出类型
    string sigle_data;
    int tmp_col_base;
    vector<string> tmp_container;
    while (getline(data_in, line)) {
        istringstream record(line);
        tmp_container.clear();
        tmp_col_base = col_base;
        while (tmp_col_base > 0) {
            --tmp_col_base;
            record >> sigle_data;
        }
        while (record >> sigle_data) {
            tmp_container.push_back(sigle_data);
        }
        container.push_back(tmp_container);
    }
    return container;
}

void Data::get_data(vector<vector<string>> &container, int col_base) {
    container = get_data(col_base);
}


// // 通过指定数据划分索引将数据划分为两部分, 
// // 在机器学习中一般指训练集与标签。
// void Data::get_data(vector<vector<string>> &left_data,
//               vector<vector<string>> &right_data, 
//               int split, int col_base) {
//     vector<vector<string>> container;
//     container = get_data(col_base);
//     int col = container[0].size();
//     if (split < 0) {
//         split = col + split;
//     }
// 	vector<string> tmp_left;
//     vector<string> tmp_right;
//     for (int r = 0; r != container.size(); ++r) {
// 		auto tmp_container = container[r];
// 		for (int c = 0; c != split; ++c) {
// 			tmp_left.push_back(tmp_container[c]);
// 		}
// 		for (int c = split; c != col; ++c) {
// 			tmp_right.push_back(tmp_container[c]);
// 		}
//         left_data.emplace_back(tmp_left);
//         right_data.emplace_back(right);
// 		tmp_left.clear();
// 		tmp_right.clear();
//     }
// }

/*********************** ~ Data ***********************/


/*********************** Trans ***********************/
void Trans::_get_data() {
    if (_p_data.size() == 0) {
        get_data(_p_data);
    }
}


// template <typename _tran_type>
// _tran_type Trans::convert_to(const std::vector<std::string> &data, const std::string &type) {
//     _tran_type new_data;
//     for (auto it = data.begin(); it != data.end(); ++it) {
//         new_data.push_back(_bin_ops[type](*it));
//     }
//     return new_data;
// }


// template <typename _tran_type>
// void Trans::convert_to(const std::vector<std::string> &data, _tran_type &new_data, const std::string &type) {
//     for (auto it = data.begin(); it != data.end(); ++it) {
//         new_data.push_back(_bin_ops[type](*it));
//     }
// }

// // new_data为空容器
// template <typename _tran_type>
// void Trans::convert_to(_tran_type &new_data, const std::string &type) {
//     // _get_data();
//     for (auto it = _p_data.begin(); it != _p_data.end(); ++it) {
//         // new_data.push_back(_bin_ops[type](*it));
//     }
// }

// template <typename _tran_type>
// _tran_type Trans::convert_to(const std::string &type) {
//     _get_data();
//     _tran_type new_data, 
//     for (auto it = _p_data.begin(); it != _p_data.end(); ++it) {
//         new_data.push_back(_bin_ops[type](*it));
//     }
//     return new_data;
// }

// template <typename _t>
// map<string, function<_t(string)>> Trans::_bin_ops = {
//     {"int", stoi},
//     {"long", stol},
//     {"unsigned long", stoul},
//     {"float", stof},
//     {"double", stod}
// };

// new_data为空容器
template <>
void Trans::convert_to(vector<vector<float>> &new_data) {
    _get_data();
    vector<float> tmp_data;
    for (auto it = _p_data.begin(); it != _p_data.end(); ++it) {
        tmp_data.clear();
        for (auto t = (*it).begin(); t != (*it).end(); ++t) {
            tmp_data.push_back(stof(*t));  
        }
        new_data.push_back(tmp_data);
    }
}

template <>
void Trans::convert_to(vector<vector<int>> &new_data) {
    _get_data();
    vector<int> tmp_data;
    for (auto it = _p_data.begin(); it != _p_data.end(); ++it) {
        tmp_data.clear();
        for (auto t = (*it).begin(); t != (*it).end(); ++t) {
            tmp_data.push_back(stoi(*t));  
        }
        new_data.push_back(tmp_data);
    }
}

template <>
void Trans::convert_to(vector<vector<double>> &new_data) {
    _get_data();
    vector<double> tmp_data;
    for (auto it = _p_data.begin(); it != _p_data.end(); ++it) {
        tmp_data.clear();
        for (auto t = (*it).begin(); t != (*it).end(); ++t) {
            tmp_data.push_back(stod(*t));  
        }
        new_data.push_back(tmp_data);
    }
}


// 转换为矩阵
void Trans::convert_to_mat(Mat &new_data) {
    for (int r = 0; r != _p_data.size(); ++r) {
        for (int c = 0; c != _p_data[0].size(); ++c) {
            new_data.at<float>(r, c) = stof(_p_data[r][c]);
        }
    }
}
/*********************** ~ Trans ***********************/


/* 获得数据 */
void get_train_data(const std::string &file_path, Mat &_feature, 
                    Mat &_labels, int col_base)
{
    cout << "[INFO] loading data." << endl;
    Data file(file_path);
    // 划分数据
	vector<vector<string>> data;
    file.get_data(data, col_base);
    Mat _data = Mat::zeros(Size(data[0].size(), data.size()), CV_32FC1);
    Trans t(data);
    t.convert_to_mat(_data);
    int col = _data.cols;
    _feature = _data.colRange(Range(0, col - 1));
    _labels = _data.colRange(Range(col - 1, col));
}