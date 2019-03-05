// segmentation_main.cpp
// 2019-3-3 ~ 3-5
// 使用softmax分割图像
// 分割图像入口
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <exception>
#include <atomic>
#include <thread>
#include <mutex>

#include<time.h>

#include "../include/MLCore.hpp"
#include "../include/ImgCore.hpp"
#include "../include/FileTool.hpp"
#include "../include/utils.hpp"


#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace cv;

using namespace std;

// static atomic<int> count(1);
static int _count = 0;
mutex g_lock;

/* 使用Softmax训练数据 */
void softmax_train(const string &train_data_path, int base_col,
				   Mat &weights, int k, long long max_iter);

/* 单独分割一张图片 */
void single_seg(string img_path, string output_dir, 
				vector<int> clip_size, Mat weights);



int main(int argc, char const *argv[])
{
	clock_t start, finish;
   	double total_time;
   	start = clock();

	string img_path = "C:\\Study\\test\\bone\\c_test_img";
	string output_dir = "C:\\Study\\test\\bone\\c_test_img_res_";
	vector<int> clip_size = { 40, -40, 40, -40 };
	vector<string> filer_patt = { ".png", ".jpg" };
	string train_data = "C:\\Study\\test\\bone\\data.txt";
	int base_col = 2;

	Mat weights;
	softmax_train(train_data, base_col, weights, 256, 2000);

    if (!folder_exist(output_dir)) {
        mkdirs(output_dir);
    }

    // 获取文件路径
    Files file(img_path);
    vector<string> files_list;
    file.get_files(files_list, filer_patt);

    int total = files_list.size();
    cout << "[INFO] total : " << total << endl;

    for (auto file : files_list) {
    	// cout << "[INFO] starting handle : " << file << endl;
    	try {
    		thread th(single_seg, file, output_dir, clip_size, weights);
    		th.detach();
    	} catch (exception e) {
    		cout << "[ERROR] " << e.what() << endl;
    	}
    }
    system("pause");
   	finish = clock();
   	total_time = (double)(finish - start) / CLOCKS_PER_SEC;
   	cout << "[INFO] finished in " << total_time << "s." << endl;
	return 0;
}


void softmax_train(const string &train_data_path, int base_col,
				   Mat &weights, int k, long long max_iter) 
{
	Mat feature, labels;
	get_train_data(train_data_path, feature, labels, base_col);
	Softmax softmax(k, max_iter);
	weights = softmax.fit(feature, labels);
}


void single_seg(string img_path, string output_dir, 
	            vector<int> clip_size, Mat weights)
{

	Mat img = imread(img_path, 0);
    int r = img.rows, c = img.cols;

    // string dirpath = path_dirpath(img_path);
    string output_path = path_join(output_dir, path_basename(img_path));
    // cout << "[DEBUG] output image path: " << output_path << endl;
    // 裁剪
    int x = clip_size[0], w = clip_size[1];
    int y = clip_size[2], h = clip_size[3];
    Mat img_resize = img(Rect(Point(x, y), Point(c + w, r + h))).clone();

    // cout << "[DEBUG] threshold. "<< endl;
    int threshed_value = get_threshed_value_by_softmax(img_resize, weights);
    Mat threshold_img;
    threshold(img_resize, threshold_img, threshed_value, 255, THRESH_BINARY);
	save_image(output_path, threshold_img, "_threshed_raw");

	// cout << "[DEBUG] segmentate image. "<< endl;
    // 使用种子生长法进行分割
    Seg seg(0);
    Mat img_seg, threshold_seg;
    seg.apply(img_resize, threshold_img, img_seg, threshold_seg);
    save_image(output_path, threshold_seg, "_threshold");

    // cout << "[DEBUG] remove margin. "<< endl;
    // 去除周围多余边缘
    Mat img_remove_margin;
    remove_margin(img_seg, threshold_seg, img_remove_margin);
    save_image(output_path, img_remove_margin, "_remove_margin");

    // cout << "[DEBUG] norm_to_size. "<< endl;
    // 归一化
    Mat img_normed;
    norm_to_size(img_remove_margin, img_normed, 256);
    save_image(output_path, img_normed, "_resize");

	// g_lock.lock();
	cout << "[INFO] handle count: " << ++_count << endl;
	cout << "[INFO] handling file: " << output_path << endl;
    // g_lock.unlock();
}