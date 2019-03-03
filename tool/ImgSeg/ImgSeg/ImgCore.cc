// ImgCore.cc

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <string>

#include <cmath>


#include "ImgCore.h"
#include "FileTool.h"

using namespace cv;
using namespace std;


/* 去噪 */
void move_noise(const Mat img_in, 
				Mat &img_out, 
				int kernel, 
				int op, 
				const int repeat) 
{
	// cout << "[INFO] call move_noise()" << endl;
	medianBlur(img_in, img_out, kernel);
	Mat element = getStructuringElement(MORPH_RECT, Size(kernel, kernel));
	for (int it = 0; it != repeat; ++it) {
       morphologyEx(img_out, img_out, op, element);
	}
}


/* 获得直方图 */
void get_histogram(const Mat img, Mat &hist) {
	// cout << "[INFO] call get_histogram()" << endl;
	Mat _hist = Mat::zeros(Size(256, 1), CV_32FC1)
	for (int r = 0; r != img.rows; ++r) {
		// cout << "[INFO] read row: " << r << endl;
		for (int c = 0; c != img.cols; ++c) {
			// cout << img <<endl;
			// cout << "[INFO] value: " << img.at<uchar>(r, c) << endl;
			int index = img.at<uchar>(r, c);
			// cout << "[INFO] value: " << index << endl;
			_hist.at<float>(0, index) += 1;
		}
	}
	hist = _hist;
}


/* 通过softmax算法获得阈值 */
int get_threshed_value_by_softmax(const Mat &img, const Mat &weight) {
    Mat hist = Mat::zeros(Size(256, 1), CV_32FC1);
    get_histogram(img, hist);
    // 归一化, https://blog.csdn.net/cosmispower/article/details/64457406
    normalize(hist, hist, 1, 0, NORM_MINMAX); 
    Mat p = hist * _weight; // p : 1 x m x m x n = 1 x n
	float max_val = MIN;
	int max_index = -1;
	for (int i = 0; i != p.cols; ++i) {
		if (p.at(0, i) > max_val) {
			max_val = p.at(0, i);
			max_index = i;
		}
	}
	return max_index;
}


/* 保存图片 */
void save_imgage(const std::string &img_path, const Mat img, const std::string &mid_name) {
	string basename = path_basename(img_path);
	vector<string> file = path_splitext(basename);
	string dir_path = path_dirpath(img_path);
	string img_name = file[0] + mid_name + file[1];
	string output_path = path_join(dir_path, img_name);
	imwrite(output_path, img);
}


/* 去除周围空白区域 */
void move_margin(const Mat img, const Mat &threshed_img, Mat &output) {
	int row = img.rows, col = img.cols;
	Rect rect = boundingRect(threshed_img);
	Point tl = rect.tl(), br = rect.br();
	if (tl.x >= 10 
		&& tl.y >= 10 
		&& (tl.x + br.x) <= row 
		&& (tl.y + br.y) <= col) 
	{
		tl.x -= 10;
		tl.y -= 10;
		br.x += 20;
		br.y += 20;
	}

	output(Rect(tl, br));
}

/* 归一化 */
void norm_to_size(const Mat img, const Mat &output, int size=256) {
	int row = img.rows, col = img.cols;
	int gap = abs(row - col);
	Mat tmp_out;
	if (row > col) {
		// 高大于宽则水平方向扩展
		Mat fill = Mat::zeros(Size(gap/2, row));
		hconcat(fill, img, tmp_out);
		hconcat(tmp_out, fill, tmp_out);
	} else {
		Mat fill = Mat::zeros(Size(col, gap/2));
		vconcat(fill, img, tmp_out);
		vconcat(tmp_out, fill, tmp_out);
	}
	resize(tmp_out, output, Size(size, size), (0, 0), (0, 0), INTER_LINEAR);
}


/* 图像分割 */

/* 区域生长法 */
void Roi_region::apply(const Mat &src, const Mat &threshed_img, Mat &dst) {
	return;
}

/* 最大连通区域 */
void Max_region::apply(const Mat &src, const Mat &threshed_img, Mat &dst) {
	return;
}

/* 分割模型选择 */
Seg::_choose_model(int model_name) {
	switch (model_name) {
		case 0 : _model = new Roi_region(); break;
		case 1 : _model = new Max_region(); break;
	}
}