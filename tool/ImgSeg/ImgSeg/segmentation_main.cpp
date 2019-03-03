// segmentation_main.cpp
// 2019-3-
// 分割图像入口
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <exception>


#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;
using namespace std;

/* 单独分割一张图片 */
void single_seg(const string &img_path, const string &output_dir, const vector<int> &clip, const Mat &weights);

/* 使用Softmax训练数据 */
void softmax_train(const string &train_data_path, Mat &weights, int k, long long max_iter);

atomic<int> count(1);

int main(int argc, char const *argv[])
{

	string img_path = "";
	string output_dir = "";
	vector<int> clip = {};
	string train_data = "";
	int base_col = 1;

	Mat weigths;
	softmax_train(train_data, weights, 256, 10000);

    if (!folder_exist(out_dir)) {
        mkdirs(out_dir);
    }

    // 获取文件路径
    Files file(pic_dir);
    vector<string> files_list;
    file.get_files(files_list, filer_patt);

    for (auto file : files_list) {
    	try {
    		cout << "[INFO] handling file: " << file << endl;
    		single_seg(file, output_dir, clip, weights);
    	} catch (exception e) {
    		cout << e << endl;
    	}
    }
	return 0;
}