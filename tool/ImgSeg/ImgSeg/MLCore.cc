// MLCore.cc

#include <vector>
#include <string>
#include <iostream>

#include <cmath>

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;
using namespace std;

#include "MLCore.h"

/*********************** Softmax***********************/

// 训练
Mat Softmax::train() {
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

}

// 预测
int Softmax::predict(Mat &test_data) {

}

 