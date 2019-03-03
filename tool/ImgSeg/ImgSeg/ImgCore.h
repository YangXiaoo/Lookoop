// ImgCore.h
// 图像处理函数

#include <string>

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

#define free_ptr(p) if(p) delete p; p = NULL;


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


/* 通过softmax算法获得阈值 */
int get_threshed_value_by_softmax(const Mat &img, const Mat &weight);

/*
 * 保存图片
 * @para img_path 图像完整路径
 * @para mid_name 图像保存后的中间名
 */
void save_imgage(const std::string &img_path, const Mat img, const std::string &mid_name="");


/* 去除周围空白区域 */
void move_margin(const Mat img, const Mat &threshed_img, Mat &out_put);

/* 归一化 */
void norm_to_size(const Mat img, const Mat &output, int size=256);

/* 图像分割 */
class Model {
 public:
 	virtual ~Model(){};
 	virtual void apply(const Mat &src, const Mat &threshed_img, Mat &dst) = 0;
};


class Roi_region : public Model {
 public:
 	void apply(const Mat &src, const Mat &threshed_img, Mat &dst);
};

class Max_region : public Model {
 public:
 	void apply(const Mat &src, const Mat &threshed_img, Mat &dst);
};


class Seg {
 public:
 	Seg(const std::string &seg_model=_model_name) : _model_name(seg_model) { _choose_model(seg_model); };
 	~Seg() {free_ptr(_model)};
 	void _choose_model(int model_name);
 	void apply(const Mat &src, const Mat &threshed_img, Mat &dst);
 private:
 	static int _model_name=0;
 	Model *_model;
}