// Files_Test.cpp
// 2019-2-23
#include <string>
#include <vector>
#include <iostream>
#include "Files.h"

using namespace std;
inline void print(vector<string> &lists, string decl);

int main(int argc, char const *argv[])
{
	string file_path("C:\\Study\\test\\bone\\1");
	cout << "strat" << endl;

	// case 0, 获取指定文件夹下所有指定格式文件的全路径
	vector<string> patt_0 = {".png"};
	// int model_0 = 0; // default
	// patt_0, model_0 are default parameter
	Files files(file_path);
	vector<string> files_list_0;
	files.get_files(files_list_0, patt_0);
	// print
	print(files_list_0, "FULL_PATH: ");

	// case 0_1
	vector<string> patt_1 = {".png", ".jpg"};
	vector<string> files_list_1;
	files.get_files(files_list_1, patt_1);
	print(files_list_1, "FULL_PATH_1: ");

	// case 0_2
	vector<string> files_list_01;
	files.get_files(files_list_01);
	print(files_list_01, "FULL_PATH_2: ");


	// case 1, 获取指定文件夹下所有指定格式文件名的全路径
	vector<string> files_list_2;
	int model_1 = 1;
	files.get_files(files_list_2, patt_1, model_1);
	print(files_list_2, "FILE_NAME: ");

	// case 2, 获取指定文件夹下的所有当前文件名, 深度为1
	vector<string> files_list_3;
	int model_2 = 2;
	files.get_files(files_list_3, patt_0, model_2);
	print(files_list_3, "CUR_FILE: ");

	// case 3, 获取指定文件夹下的所有当前文件夹名称, 深度为1
	vector<string> files_list_4;
	int model_3 = 3;
	vector<string> patt_2 = {};
	files.get_files(files_list_4, patt_2, model_3);
	print(files_list_4, "CUR_DIR: ");


	// 通过使用枚举
	// error
	// vector<string> files_list_5;
	// files.get_files(files_list_5, patt_1, Files::FULL_PATH);
	// print(files_list_5, "use enum: ");

	system("pause");
	return 0;
}

void print(vector<string> &lists, string decl) {
	for (const auto it : lists) 
		cout << decl << it << endl;
}