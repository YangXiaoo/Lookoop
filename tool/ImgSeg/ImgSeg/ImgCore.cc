// ImgCore.cc

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace cv;

/* 去噪 */
void move_noise(const Mat img_in, 
				Mat &img_out, 
				const int kernel, 
				int op, 
				const int repeat) {
	medianBlur(img_in, img_out, kernel);
	Mat element = getStructuringElement(MORPH_RECT, Size(kernel, kernel));
	for (int it = 0; it != repeat; ++it) {
       morphologyEx(img_out, img_out, op, element);
	}
}


/* 获得直方图 */
void get_histogram(const Mat img, Mat &hist) {
	for (int r = 0; r != img.rows; ++r) {
		const int *ptr = m.ptr<int>(r);
		for (int c = 0; c != img.cols; ++c) {
			int index = ptr[c];
			hist.at<int>(index, 0) += 1;
		}
	}
}