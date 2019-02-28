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
 	virtual Mat train() = 0;
 	virtual int predict() = 0;
 	virtual float cal_error() = 0;
};

// softmax多分类
class Softmax : public Model {
 public:
 	Mat train();
 	int predict();
 	float cal_error();
 private:
 	// 权重
 	Mat weight;
};



class ML {
 public:
 	ML() = default;
 	// softmax构造
 	ML(const std::string &ml_name, 
 	   const Mat &feature, 
 	   const Mat labels, int k, 
 	   long long max_iter, float alpha=0.1) noexcept { _choose_model(ml_name); };
 	// 训练
 	Mat train() { _model->train(); };
 	// 预测
 	int predict() {  _model->train(); };
 	// 根据名字选择接口
 	void _choose_model(const std::string &ml_name);
 private:
 	Model* _model;
 	std::string _model_name;
};
#endif