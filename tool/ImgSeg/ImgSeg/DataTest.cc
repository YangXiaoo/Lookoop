// DataTest.cc
// 读取文件测试
#include <vector>
#include <iostream>
#include "utils.h"

using namespace std;

int main(int argc, char const *argv[])
{
	Data file("C:\\Study\\test\\bone\\2_threshed\\data.txt");
	// Data data = {"C:\\Study\\test\\bone\\2_threshed\\data.txt"};
	vector<vector<string>> img_data;
	// vector<float> img_data = file.get_data<float>(1);
	file.get_data(img_data, 1);
	cout << "data[0][0]: " << img_data[0][0] << endl;

	Trans t(img_data);
	vector<vector<float>> t_data_2;
	t.convert_to(t_data_2);
	cout << "t_data_2[0][0]: " << t_data_2[0][0] << endl;

	// 划分数据
	vector<vector<string>> feature;
	vector<vector<string>> labels;
	file.get_data(feature, labels, -1, 1);
	Mat fea = Mat::zeros(Size(feature.size(), feature[0].size()), CV_32FC1);
	Mat val = Mat::zeros(Size(labels.size(), labels[0].size()), CV_32FC1)
	Trans t(feature);
	t.convert_to_mat(fea);
	Trans t(labels);
	t.convert_to_mat(val);

	cout << val.size() << endl;
	return 0;
}
