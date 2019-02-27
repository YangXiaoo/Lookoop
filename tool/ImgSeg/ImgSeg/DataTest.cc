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
	vector<string> img_data;
	// vector<float> img_data = file.get_data<float>(1);
	file.get_data(img_data);
	cout << "data[0]: " << img_data[0] << endl;

	Trans t(img_data);
	vector<float> t_data_2;
	t.convert_to(t_data_2, "double");
	cout << "t_data_2[0]: " << t_data_2[0] << endl;


	return 0;
}

