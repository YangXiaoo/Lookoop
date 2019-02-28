// MLCore.hpp
// 使用策略模式编写机器学习类

#include <vector>
#include <string>
#include <map>
#include <functional>

// OpenCV
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

#ifndef ML_CORE
#define ML_CORE

#define free_ptr(p) if(p) delete p; o = NULL;

// 抽象基
class Model {
 public:
 	virtual ~Model(){};
 	virtual void train() = 0;
 	virtual void predict() = 0;
 	virtual void cal_error() = 0;
};

class Softmax : public Model {

};

class ML {
 public:
 	Ml() = default;
 	ML(const std::string &ml_name)
 	void train();
 private:
 	int 
};
#endif