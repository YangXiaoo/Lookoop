// MLCore.cc

#include <vector>
#include <string>
#include <iostream>

#include <cmath>

#include "opencv2/core/core.hpp"

using namespace cv;
using namespace std;

#include "MLCore.h"

#define MAX 0x3f3f3f3f
#define MIN  0xc0c0c0c0
/*********************** Softmax***********************/
float _sum(Mat data) {
	// cout << "[DEBUG] call _sum(): " 
	// 	 << "data.rows: " << data.rows 
	// 	 << ", data.cols: " << data.cols << endl;
	// cout << "[DEBUG] cur val: " << data.at<float>(0, 0) << endl;
	float total = 0.0;
	for (int r = 0; r != data.rows; ++r) {
		for (int c = 0; c != data.cols; ++c) {
			total += data.at<float>(r, c);
		}
	}
	// cout << "[DEBUG] total: " << total << endl;
	return total;
}
// 训练
Mat Softmax::fit(const Mat &feature, const Mat labels) {
	// _feature = feature; // mxn

	labels.convertTo(_labels, CV_8UC1);
	feature.convertTo(_feature, CV_32FC1);
	normalize(_feature, _feature, 1, 0, NORM_MINMAX);
	// cout << "[DEBUG] cur _feature val: " << _feature.at<float>(0, 0) << endl;
	int m = _feature.rows, n = _feature.cols;
	_weight = Mat::ones(Size(_k, n), CV_32FC1); // nx_k
	int it = 0;
	float gap = 1, error_rate, pre = 1e5;
	Mat y, row_sum, _row_sum, tmp_mul; //  = Mat::zeros(Size(_k, m), CV_32FC1);
	while (it <= _max_iter && gap > _min_error) {
		// tmp_mul = _feature * _weight;
		// cout << "[DEBUG] cur tmp_mul val: " << tmp_mul.at<float>(0, 0) << endl;
		cv::exp(_feature * _weight, y); // mx_k
		// cout << "[DEBUG] cur y val: " << y.at<float>(0, 0) << endl;
		if (it % 10 == 0) {
			// cout << "[DEBUG] call cal_error()" << endl;
			error_rate = cal_error(y);
			gap = abs(error_rate - pre);
			pre = error_rate;
			cout << "[INFO] iteration: " << it
				 << ", error rate: " << error_rate
				 << ", gap: " << gap << endl;
		}
		// cout << "[DEBUG] call reduce()" << endl;
		reduce(-y, row_sum, 1, CV_REDUCE_SUM);
		// cout << "[DEBUG] call repeat()" << endl;
		repeat(row_sum, 1, _k, _row_sum);
		// cout << "[DEBUG] y.rows: " << y.rows
		// 	 << ", y.cols: " << y.cols
		// 	 << endl;
		// cout << "[DEBUG] row_sum.rows: " << row_sum.rows
		// 	 << ", row_sum.cols: " << row_sum.cols
		// 	 << endl;
		y = y / _row_sum;
		for (int x = 0; x != m; ++x) {
			y.at<float>(x, _labels.at<uchar>(x, 0)) += 1.0;
		}
		_weight += (_alpha / m) * _feature.t() * y;
		++it;
	}
	return _weight;
}

// 计算误差
float Softmax::cal_error(Mat err) {
	int m = err.rows; // mx_k
	float sum_cost = 0.0;
	for (int i = 0; i != m; ++i) {
		if (err.at<float>(i, _labels.at<uchar>(i, 0)) / _sum(err.rowRange(Range(i, i+1))) > 0) {
			// cout << "[DEBUG] if : ok" << endl;
			sum_cost -= log(err.at<float>(i, _labels.at<uchar>(i, 0)) / _sum(err.rowRange(Range(i, i+1))));
		} else {
			sum_cost -= 0;
		}
	}
	return sum_cost / m;
}

// 预测
int Softmax::predict(const Mat &test_data) {
	Mat p = test_data * _weight; // p : 1 x m x m x n = 1 x n
	float max_val = MIN;
	int max_index = -1;
	for (int i = 0; i != p.cols; ++i) {
		if (p.at<float>(0, i) > max_val) {
			max_val = p.at<float>(0, i);
			max_index = i;
		}
	}
	return max_index;
}
/*********************** ~Softmax***********************/