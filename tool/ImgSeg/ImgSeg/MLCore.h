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
 	Softmax(int k, long long max_iter, float alpha=0.1, float min_error=0.0001) 
 		    : _k(k), _max_iter(max_iter), _alpha(alpha), _min_error(min_error) {};
 	Mat fit(const Mat &feature, const Mat labels);
	int predict(const Mat &test_data);
 	float cal_error(Mat err);
 private:
 	// 权重
 	Mat _weight;
 	Mat _feature;
 	Mat _labels;
 	int _k;
 	long long _max_iter;
 	float _min_error; 
 	float _alpha;
};
#endif