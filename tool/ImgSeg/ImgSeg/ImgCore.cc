// ImgCore.cc

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <string>
#include <vector>
#include <deque>

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
	Mat _hist = Mat::zeros(Size(256, 1), CV_32FC1);
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
    Mat p = hist * weight; // p : 1 x m x m x n = 1 x n
	float max_val = -1;
	int max_index = -1;
	for (int i = 0; i != p.cols; ++i) {
		if (p.at<float>(0, i) > max_val) {
			max_val = p.at<float>(0, i);
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
void remove_margin(const Mat img, const Mat &threshed_img, Mat &output) {
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
void norm_to_size(const Mat img, const Mat &output, int size) {
	int row = img.rows, col = img.cols;
	int gap = abs(row - col);
	Mat tmp_out;
	if (row > col) {
		// 高大于宽则水平方向扩展
		Mat fill = Mat::zeros(Size(gap/2, row), CV_8UC1);
		hconcat(fill, img, tmp_out);
		hconcat(tmp_out, fill, tmp_out);
	} else {
		Mat fill = Mat::zeros(Size(col, gap/2), CV_8UC1);
		vconcat(fill, img, tmp_out);
		vconcat(tmp_out, fill, tmp_out);
	}
	resize(tmp_out, output, Size(size, size), (0, 0), (0, 0), INTER_LINEAR);
}


/* 图像分割 */

/* 区域生长法 */
void Roi_region::apply(const Mat &src, const Mat &threshed_img, 
	        		   Mat &dst_src, Mat &dst_threshed) 
{
	int row = src.rows, col = src.cols;
	int mid_r = row / 2, mid_c = col /2; // 种子
	vector<vector<bool>> visited(row, vector<bool>(col, false));
	deque<vector<int>> dequeue;
	dequeue.push_back({mid_r, mid_c});
	visited[mid_r][mid_c] = true;
	while (!dequeue.empty()) {
		long size = dequeue.size();
		while (size != 0) {
			vector<int> _tmp = dequeue.back();
			dequeue.pop_back();
			int r = _tmp[0], c = _tmp[1];
			// up
			if (r > 0 && !visited[r - 1][c] && threshed_img.at<uchar>(r - 1, c) != 0) {
				dequeue.push_front({r - 1, c});
				visited[r - 1][c] = true;
			}

			// right
			if (c < col - 1 && !visited[r][c + 1] && threshed_img.at<uchar>(r, c + 1) != 0) {
				dequeue.push_front({r, c + 1});
				visited[r][c + 1] = true;
			}

			// down
			if (r < row - 1 && !visited[r + 1][c] && threshed_img.at<uchar>(r + 1, c) != 0) {
				dequeue.push_front({r + 1, c});
				visited[r + 1][c] = true;
			}

			// left
			if (c > 0 && !visited[r][c - 1] && threshed_img.at<uchar>(r, c - 1) != 0) {
				dequeue.push_front({r, c - 1});
				visited[r][c - 1] = true;
			}
			--size;
		}
	}

	dst_src = src.clone();
	dst_threshed= threshed_img.clone();
	for (int r = 0; r != row; ++r) {
		for (int c = 0; c != col; ++col) {
			if (!visited[r][c]) {
				dst_src.at<uchar>(r, c) = 0;
				dst_threshed.at<uchar>(r, c) = 0;
			}
		}
	}
	return;
}

/* 最大连通区域 */
void Max_region::apply(const Mat &src, const Mat &threshed_img, 
					   Mat &dst_src, Mat &dst_threshed) 
{

	int row = src.rows, col = src.cols;
	long max_count = 0;
	vector<vector<bool>> max_visited;
	for (int _r = 0; _r != row; ++_r) {
		for (int _c = 0; _c != col; ++_c) {
			vector<vector<bool>> visited(row, vector<bool>(col, false));
			deque<vector<int>> dequeue;
			dequeue.push_back({_r, _c});
			long tmp_count = 0;
			visited[_r][_c] = true;
			while (!dequeue.empty()) {
				long size = dequeue.size();
				while (size != 0) {
					vector<int> _tmp = dequeue.back();
					dequeue.pop_back();
					int r = _tmp[0], c = _tmp[1];
					// up
					if (r > 0 && !visited[r - 1][c] && threshed_img.at<uchar>(r - 1, c) != 0) {
						dequeue.push_front({r - 1, c});
						visited[r - 1][c] = true;
						++tmp_count;
					}

					// right
					if (c < col - 1 && !visited[r][c + 1] && threshed_img.at<uchar>(r, c + 1) != 0) {
						dequeue.push_front({r, c + 1});
						visited[r][c + 1] = true;
						++tmp_count;
					}

					// down
					if (r < row - 1 && !visited[r + 1][c] && threshed_img.at<uchar>(r + 1, c) != 0) {
						dequeue.push_front({r + 1, c});
						visited[r + 1][c] = true;
						++tmp_count;
					}

					// left
					if (c > 0 && !visited[r][c - 1] && threshed_img.at<uchar>(r, c - 1) != 0) {
						dequeue.push_front({r, c - 1});
						visited[r][c - 1] = true;
						++tmp_count;
					}
					
					--size;
				}
			}

			if (tmp_count > max_count) {
				max_count = tmp_count;
				max_visited = visited;
			}
		}
	}
	dst_src = src.clone();
	dst_threshed= threshed_img.clone();
	for (int r = 0; r != row; ++r) {
		for (int c = 0; c != col; ++col) {
			if (!max_visited[r][c]) {
				dst_src.at<uchar>(r, c) = 0;
				dst_threshed.at<uchar>(r, c) = 0;
			}
		}
	}
	return;
}

/* 分割模型选择 */
void Seg::_choose_model(int model_name) {
	switch (model_name) {
		case 0 : _model = new Roi_region(); break;
		case 1 : _model = new Max_region(); break;
	}
}