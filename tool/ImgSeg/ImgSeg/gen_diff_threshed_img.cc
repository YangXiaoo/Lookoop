// gen_diff_threshed_img.cpp
// 选择最佳阈值
// 2019-2-25

#include<iostream>
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

using namespace cv;
using namespace std;

// mutex mt;
// atomic<int> count(1);

/* 生成单张图片并保存 */
void _generate_pic(Mat src, double value, 
                  double mean_value, string out_dir, 
                  string pic_path);
/* 生成不用阈值分割的图片 */
void gen_diff_threshed_img(const string &pic_dir, 
                           const string &out_dir,
                           const vector<string> filer_patt,
                           const vector<int> &clip_size);
/* 生成不同范围的阈值 */
vector<int> _generate_threshed_val(double mean_value);


int main(int argc, char const *argv[])
{
    string pic_dir = {""};
    string out_dir = {""};
    vector<string> filer_patt = {".png", ".jpg"};
    vector<int> clip_size = {40, -40, 40, -40};
    gen_diff_threshed_img(pic_dir, out_dir, filer_patt, clip_size);
    return 0;
}


void gen_diff_threshed_img(const string &pic_dir, 
                           const string &out_dir,
                           const vector<string> filer_patt,
                           const vector<int> &clip_size) 
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

    ofstream file_record(out_record);
    ofstream img_data(out_data);
    ofstream labels(out_lables);

    int count = 0;
    for (auto &file : files_list) {
        cout << "[INFO] generate: " << file << endl;

        file_record << count << " " << file << "\n";

        Mat img = imread(file, 0);

        int m = img.rows, n = img.cols;
        int x = clip_size[0], w = clip_size[1];
        int y = clip_size[2], h = clip_size[3];

        // 裁剪
        Mat img_resize = img(Rect(x, y, m + w, n + h)).clone();

        Mat img_mv_noise;
        // 去噪
        move_noise(img_resize, img_mv_noise, 5, MORPH_CLOSE);

        // 不需要
        // double mean_value = mean(img_mv_noize)[0];
        Mat img_mean, img_sd;
        meanStdDev(img_mv_noize, img_mean, img_sd);
        double mean_value = img_mean.at<double>(0,0);
        double sd_mean = img_sd.at<double>(0,0);

        // 计算直方图
        Mat hist = Mat::zeros(Size(256, 1), cv_32UC1);
        get_histogram(img_mv_noise, hist);

        
        for (int r = 0; r != hist.rows; ++r) {
            img_data << count << " ";
            for (int c = 0; c != hist.cols; ++c) {
                img_data << hist.at<int>(r, c) << " ";
            }
        }
        img_data << "\n";

        labels << count << " " << "\n";

        vector<double> threshed_value;
        threshed_value.emplace(gen_range(0, mean_value, -2, 20));
        threshed_value.emplace(gen_range(mean_value+2, 255, 2, 5));

        for (auto value : threshed_value) {
            thread th_gen(_generate_pic, img_mv_noise, value, mean_value, out_dir, file);
            th_gen.detach();
        }
    }

    // 关闭文件流
    file_record.close();
    img_data.close();
    labels.close();
}


void _generate_pic(Mat src, double value, 
                  double mean_value, string out_dir, 
                  string pic_path) {
        Mat dst;
        threshold(src, dst, value, 255, THRESH_BINARY)；
        move_noise(img_resize, img_mv_noise, 5, MORPH_CLOSE);
        // 保存
        string base_name = path_basename(pic_path);
        vector<string> file = path_splitxt(pic_path);

        ostringstream rename_file;

        if (mean_value == value) 
            rename_file << file[0] << "_threshed_value_" 
                        << value << "_mean" << file[1];
        else
            rename_file << file[0] << "_threshed_value_"
                        << value << file[1];

        string new_path = path_join(out_dir, rename_file.str());
        imwrite(new_path, dst);
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