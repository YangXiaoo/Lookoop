// gen_diff_threshed_img.cpp
// 选择最佳阈值
// 2019-2-25

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include <thread>
// #include <mutex>
// #include <atomic>

#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"


#include "FileTool.h"
#include "ImgCore.h"
#include "utils.h"

using namespace cv;
using namespace std;

// mutex mt;
// atomic<int> count(1);

/* 生成单张图片并保存 */
void _generate_pic(Mat src, double value, 
                  double mean_value, string out_dir, 
                  string pic_path, int pic_number);
/* 生成不用阈值分割的图片 */
void gen_diff_threshed_img(const string pic_dir, 
                           string out_dir,
                           const vector<string> filer_patt,
                           const vector<int> clip_size);
///* 生成不同范围的阈值 */
//vector<int> _generate_threshed_val(double mean_value);

void _generate_pic(Mat src, double value,
				   double mean_value, string out_dir,
				   string pic_path, int pic_number) {
	cout << "[INFO] generating image path: " << pic_path << endl;
	Mat _dst, dst;
	threshold(src, _dst, value, 255, THRESH_BINARY);
	move_noise(_dst, dst, 5, MORPH_CLOSE);
	// 保存
	string base_name = path_basename(pic_path);
	vector<string> file = path_splitext(base_name);

	ostringstream rename_file;

	if ((int)mean_value == (int)value)
		rename_file << pic_number << "_" << file[0] << "_threshed_value_"
		<< value << "_mean" << file[1];
	else
		rename_file << pic_number << "_" << file[0] << "_threshed_value_"
		<< value << file[1];

	string new_path = path_join(out_dir, rename_file.str());
	imwrite(new_path, dst);
}


void gen_diff_threshed_pic(const string pic_dir, 
                           string out_dir,
                           const vector<string> filer_patt,
                           const vector<int> clip_size) 
{   
    if (!folder_exist(out_dir)) {
        mkdirs(out_dir);
    }

    // 获取文件路径
    Files file(pic_dir);
    vector<string> files_list;
    file.get_files(files_list, filer_patt);
    // print
    for (const auto it : files_list) {
        cout << "[INFO] file path: " << it << endl;
    }

    string out_lables, out_data, out_record;
    out_lables = path_join(out_dir, "labels.txt");
    out_data = path_join(out_dir, "data.txt");
    out_record = path_join(out_dir, "record.txt");
    // print
    // cout << "[INFO] output files path:" << endl;
    cout << out_lables << endl;
    cout << out_data << endl;
    cout << out_record << endl;
         
    ofstream file_record(out_record);
    ofstream img_data(out_data);
    ofstream labels(out_lables);

    int count = 0;
    for (auto &file : files_list) {
        ++count;
        cout << "[INFO] processing: " << file << endl;

        file_record << count << " " << file << "\n";

        Mat img = imread(file, 0);
        // cout << "[INFO] img channel: " << img.channels() << endl;

        int r = img.rows, c = img.cols;
        int x = clip_size[0], w = clip_size[1];
        int y = clip_size[2], h = clip_size[3];
        // print
        // cout << "[INFO] r, c, x, w, y, h: " << r << " "
        //      << c << " " << x << " " << w << " " 
        //      << y << " " << h <<endl;

        // 裁剪
        Mat img_resize = img(Rect(Point(x, y), Point(c + w, r + h))).clone();

        Mat img_mv_noise;
        // 去噪
        move_noise(img_resize, img_mv_noise, 5, MORPH_CLOSE);

        // 不需要
        // double mean_value = mean(img_mv_noize)[0];
        Mat img_mean, img_sd;
        meanStdDev(img_mv_noise, img_mean, img_sd);
        double mean_value = img_mean.at<double>(0, 0);
        double sd_mean = img_sd.at<double>(0, 0);

        // 计算直方图
        Mat hist;
        get_histogram(img_mv_noise, hist);

        cout << "[INFO] writing image histogram data." << endl;
        img_data << count << " ";
        for (int r = 0; r != hist.rows; ++r) {
            for (int c = 0; c != hist.cols; ++c) {
                img_data << hist.at<float>(c) << " ";
            }
        }
        img_data << "\n";

        labels << count << " " << "\n";

        vector<int> threshed_value;
		int mean = mean_value;
		gen_range(threshed_value, 0, mean, -2, 20);
		gen_range(threshed_value, mean+2, 255, 2, 5);

        for (auto value : threshed_value) {
            thread th_gen(_generate_pic, img_mv_noise, value, mean_value, out_dir, file, count);
            th_gen.detach();
        }
    }

    // 关闭文件流
    file_record.close();
    img_data.close();
    labels.close();
}


vector<int> _generate_threshed_val(double mean_value) {
    int low_count = 20, high_count = 5, threshed_gap = 2;
    vector<int> threshed_value;

    int gen_count = 0, tmp_val = mean_value;
    while (tmp_val > 0 && gen_count < low_count) {
        threshed_value.push_back(tmp_val);
        tmp_val -= threshed_gap;
        gen_count += 1;
    }

    gen_count = 0; 
    tmp_val = mean_value;
    while (tmp_val < 255 && gen_count <high_count) {
        tmp_val += threshed_gap;
        threshed_value.push_back(tmp_val);
        gen_count += 1;
    }

    return threshed_value; 
}



// 运行
// int main(int argc, char const *argv[])
// {
// 	string pic_dir; //  = { "C:\\Study\\test\\bone\\2" };
// 	string out_dir; //  = { "C:\\Study\\test\\bone\\2_threshed" };
//     cout << "input image dir: " << endl;
//     cin >> pic_dir;
//     cout << "input output dir: " << endl;
//     cin >> out_dir;
// 	vector<string> filer_patt = { ".png", ".jpg" };
// 	vector<int> clip_size = { 40, -40, 40, -40 };

//     // // test
//     // if (!folder_exist(out_dir)) {
//     //     cout << mkdirs(out_dir) << endl;
//     // }

// 	gen_diff_threshed_pic(pic_dir, out_dir, filer_patt, clip_size);
//     system("pause");
// 	return 0;
// }