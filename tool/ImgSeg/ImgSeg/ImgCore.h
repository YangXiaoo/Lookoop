// ImgCore.h
// 图像处理函数

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

/* 去除噪音
op:
	MORPH_OPEN – 开运算（Opening operation）
	MORPH_CLOSE – 闭运算（Closing operation）
	MORPH_GRADIENT -形态学梯度（Morphological gradient）
	MORPH_TOPHAT - “顶帽”（“Top hat”）
	MORPH_BLACKHAT - “黑帽”（“Black hat“）
 */
void move_noise(const Mat img_in, 
				Mat &img_out, 
				int kernel, 
				int op, 
				const int repeat=5);

/* 获得直方图 */
void get_histogram(const Mat img, Mat &hist);

