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
// 训练
Mat Softmax::fit(const Mat &feature, const Mat labels) {
	_feature = feature;
	_labels = labels;
	int m = _feature.rows, n = _feature.cols;
	_weight = Mat::ones(Size(n, k), CV_32FC1);
	int it = 0;
	float pre = 1e5, gap = 1, error_rate;
	Mat y, row_sum = Mat::zeros(Size(m, 1), CV_32FC1);
	Mat _row_sum;
	while (it <= _max_iter && gap > _min_error) {
		exp(_feature * _weight, y);
		if (it % 500 == 0) {
			error_rate = cal_error(y);
			gap = abs(error_rate - pre);
			pre = error_rate;
			cout << "iteration: " << it
				 << ", error rate: " << error_rate
				 << ", gap: " << gap << endl;
		}
		reduce(-y, row_sum, 1, CV_REDUCE_SUM);
		repeat(row_sum, k, 1, _row_sum);
		y = y / _row_sum;
		for (int x = 0; x != m; ++x) {
			y.at(x, _labels.at<int>(x, 0)) += 1;
		}
		_weight += (_alpha / m) * _feature.t() * y;
		++it;
	}
	return _weight
}

// 计算误差
float Softmax::cal_error(Mat err) {
	int m = err.rows;
	float sum_cost = 0.0;
	for (int i = 0; i != m, ++i) {
		if (err.at(i, _labels.at<int>(i, 0)) / sum(err.rowRange(Range(i, i+1))) > 0) {
			sum_cost -= log(err.at(i, _labels.at<int>(i, 0)) / sum(err.rowRange(Range(i, i+1))));
		} else {
			sum_cost -= 0
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
		if (p.at(0, i) > max_val) {
			max_val = p.at(0, i);
			max_index = i;
		}
	}
	return max_index;
}