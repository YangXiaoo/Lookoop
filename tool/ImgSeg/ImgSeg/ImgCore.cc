// ImgCore.cc

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>

#include "ImgCore.h"
using namespace cv;
using namespace std;


/* 去噪 */
void move_noise(const Mat img_in, 
				Mat &img_out, 
				int kernel, 
				int op, 
				const int repeat) {
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
	for (int r = 0; r != img.rows; ++r) {
		// cout << "[INFO] read row: " << r << endl;
		for (int c = 0; c != img.cols; ++c) {
			// cout << img <<endl;
			// cout << "[INFO] value: " << img.at<uchar>(r, c) << endl;
			int index = img.at<uchar>(r, c);
			// cout << "[INFO] value: " << index << endl;
			hist.at<float>(0, index) += 1;
		}
	}
}


