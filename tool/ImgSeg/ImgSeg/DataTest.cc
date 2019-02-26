// DataTest.cc
// 读取文件测试

int main(int argc, char const *argv[])
{
	Data data("C:\\Study\\test\\bone\\2_threshed\\data.txt");
	// Data data = {"C:\\Study\\test\\bone\\2_threshed\\data.txt"};
	vector<float> img_data;
	data.get_data(img_data);
	return 0;
}