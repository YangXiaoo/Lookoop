// MLCore.hpp

// OpenCV
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

#ifndef ML_CORE
#define ML_CORE

#define free_ptr(p) if(p) delete p; p = NULL;

// softmax多分类
class Softmax {
 public:
 	Softmax() = default;
 	Softmax(const Mat &feature, 
 	   		const Mat labels, int k, 
 	   		long long max_iter, float alpha=0.1, float min_error=0.0001) 
 		    : _feature(feature), _labels(labels), _max_iter(max_iter), _alpha(alpha), _min_error(min_error) {};
 	Mat train();
 	int predict(Mat &test_data);
 	float cal_error(Mat err);
 private:
 	// 权重
 	Mat weight;
 	Mat _feature;
 	Mat _labels;
 	long long _max_iter;
 	float _min_error; 
 	float _alpha;
};

#endif