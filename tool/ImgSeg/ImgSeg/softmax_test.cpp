// softmax_test.cpp
// 2019-3-3


#include <iostream>
#include <string>

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;


#include "MLCore.h"
#include "ImgCore.h"
#include "FileTool.h"

using namespace std;


int main(int argc, char const *argv[])
{
	string data_path = "";
	Mat feature, labels;
	get_train_data(data_path, feature, labels, 1);
	int k = 256;
	long long max_iter = 10000;
	Softmax softmax(k, max_iter);
	Mat weights = softmax.fit(feature, labels);

	// 获得测试图片
	string img_path = "";
	Mat test_img = imread(img_path, 0);
    Mat hist;
    // cout << "[INFO] hist.size(): " << hist.size() << endl;
    get_histogram(test_img, hist);
    int threshed_value = softmax.predict(hist);
    cout <<  "[INFO] prediction of image threshed value: " << threshed_value << endl;
	return 0;
}
