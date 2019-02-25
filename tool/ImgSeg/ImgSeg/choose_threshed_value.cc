// choose_threshed_value.cpp
// 人工选择最佳阈值
// 2019-2-25

#include<iostream>
#include <fstream>
#include <string>
#include <sstream>

#include "FileTool.h"
#include "ImgCore.h"

void choose_threshed_value(const string &pic_dir, 
						   const string &out_dir,
						   vector<string> filer_patt,
						   vector<int> &clip_size) 
{	
	if (!folder_exist(out_dir)) {
		mkdirs(out_dir);
	}

	// 获取文件路径
	Files file(pic_dir);
	vector<string> files_list;
	file.get_files(files_list, filer_patt);

	string out_lables, out_data, out_record;
	out_lables = path_join(out_dir, "labels.txt");
	out_dir = path_join(out_dir, "data.txt");
	out_record = path_join(out_dir, "record.txt");

	int count = 0;
	for (auto &file : files_list) {
		ostringstream ostring;
		ostring << count << " " << file << "\n";

		Mat img = imread(file, 0);

	    int m = img.rows, n = img.cols;
	    int x = clip_size[0], w = clip_size[1];
	    int y = clip_size[2], h = clip_size[3];

	    // 裁剪
	    Mat img_resize = img(Range(x, m + w), Range(y, n + h));

	    Mat 

	}


}