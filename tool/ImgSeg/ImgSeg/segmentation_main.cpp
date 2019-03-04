// segmentation_main.cpp
// 2019-3-
// 分割图像入口
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <exception>
#include <atomic>
#include <thread>
#include <mutex>

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;
using namespace std;


/* 使用Softmax训练数据 */
void softmax_train(const string &train_data_path, Mat &weights, 
				   int k, long long max_iter);

/* 单独分割一张图片 */
void single_seg(const string &img_path, const string &output_dir, 
				const vector<int> &clip, const Mat &weights);


atomic<int> count(1);
mutex g_lock;

int main(int argc, char const *argv[])
{

	string img_path = "";
	string output_dir = "";
	vector<int> clip_size = { 40, -40, 40, -40 };
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

    int total = files_list.size();
    cout << "[INFO] total : " << total << endl;

    for (auto file : files_list) {
    	try {
    		thread th(single_seg, file, output_dir, clip, weights);
    		th.detach();
    	} catch (exception e) {
    		cout << e.what() << endl;
    	}
    }
	return 0;
}


void softmax_train(const string &train_data_path, Mat &weights, 
				   int k, long long max_iter) 
{
	Mat feature, labels;
	get_train_data(data_path, feature, labels, 1);
	Softmax softmax(k, max_iter);
	weights = softmax.fit(feature, labels);
}


void single_seg(const string &img_path, const string &output_dir, 
	            const vector<int> &clip, const Mat &weights)
{
	Mat img = imread(img_path, 0);
    int r = img.rows, c = img.cols;

    string dirpath = path_dirpath(img_path);
    string output_path = dirpath + path_basename(img_path);
    // 裁剪
    int x = clip_size[0], w = clip_size[1];
    int y = clip_size[2], h = clip_size[3];
    Mat img_resize = img(Rect(Point(x, y), Point(c + w, r + h))).clone();

    int threshed_value = get_threshed_value_by_softmax(img_resize, weights);
    Mat threshold_img;
    threshold(img_resize, threshold_img, threshed_value, 255, THRESH_BINARY);
    save_image(output_path, threshold_img, "_threshed_raw");

    // 使用种子生长法进行分割
    Seg seg(0);
    Mat img_seg, threshold_seg;
    seg.apply(img_resize, threshold_img, img_seg, threshold_seg);
    save_image(output_path, threshold_seg, "_threshold");

    // 去除周围多余边缘
    Mat img_remove_margin;
    remove_margin(img_seg, threshold_seg, img_remove_margin);
    save_image(output_path, img_remove_margin, "_remove_margin");

    // 归一化
    Mat img_normed;
    norm_to_size(img_remove_margin, img_normed, 256);
    save_image(output_path, img_normed, "_resize");

    g_lock.lock();
    cout << "[INFO] handle count: " << ++count << endl;
    cout << "[INFO] handling file: " << file << endl;
    g_lock.unlock();
}