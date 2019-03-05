// // softmax_test.cpp
// // 2019-3-4


// #include <iostream>
// #include <string>

// #include "opencv2/core/core.hpp"
// #include "opencv2/imgproc/imgproc.hpp"
// #include "opencv2/highgui/highgui.hpp"
// using namespace cv;


// #include "MLCore.h"
// #include "ImgCore.h"
// #include "FileTool.h"
// #include "utils.h"

// using namespace std;


// int main(int argc, char const *argv[])
// {
// 	string data_path = "C:\\Study\\test\\bone\\data.txt";
// 	Mat feature, labels;
// 	get_train_data(data_path, feature, labels, 2);
// 	cout << "[DEBUG] feature.rows: " << feature.rows
// 	     << ", feature.cols: " << feature.cols
// 	     << endl;
// 	cout << "[DEBUG] laels.rows: " << labels.rows
// 		 << ", labels.cols: " << labels.cols
// 		 << endl;
// 	int k = 256;
// 	long long max_iter = 10000;
// 	cout << "[INFO] training." << endl;
// 	Softmax softmax(k, max_iter);
// 	Mat weights = softmax.fit(feature, labels);

// 	// 获得测试图片
// 	string img_path = "C:\\Study\\test\\bone\\2\\fm-1-1.02.png";
// 	Mat test_img = imread(img_path, 0);
//     Mat hist;
//     // cout << "[INFO] hist.size(): " << hist.size() << endl;
//     get_histogram(test_img, hist);
//     int threshed_value = softmax.predict(hist);
//     cout <<  "[INFO] prediction of image threshed value: " << threshed_value << endl;
// 	return 0;
// }
