// 2019-2-25
Mat(int rows, int cols, int type);
// type:
// 	CV_8UC(n) : CV_8UC1-一通道，每个数值占8bit
// 	CV_8SC(n), CV_16SC(n), CV_16UC(n), CV_32SC(n), CV_32FC(n), CV_64FC(n)
Mat(Size(int cols, int rows), int type);
Mat m = Mat::ones(2, 3, CV_32FC1);
Mat m = Mat::zeros(2, 3, CV_32FC1);
Mat m = (Mat_<int>(2, 3) << 1, 2, 3, 4, 5, 6);

// 单通道信息
m.rows;
m.cols;

Size size = m.size();
m.channels();
m.total();
m.dims();
m.at<int>(r, c);
m.at<int>(Point(c, r));

// 利用ptr遍历
for (int r = 0; r < m.rows; ++r) {
	// 得到矩阵m的第r行行首的地址
	const int *ptr = m.ptr<int>(r);
	for (int c = 0; c < m.cols; ++c) {
		cout << ptr[c] << ", ";
	}
	cout << endl;
}

// 利用isContinuous遍历
if (m.isContinuous()) {
	int *ptr = m.ptr<int>(0);
	for (int n = 0; n < m.rows * m.cols; ++n) {
		cout << ptr[n] << ", ";
	}
}




// Vec
Vec(Typename _Tp, int _cn);

Vec<int, 3> vc(1, 2, 3);
vc.rows; // 3
vc.cols; // 1

vc[0]; // 1
typedef Vec<uchar, 3> Vec3b;
typedef Vec<int, 2> Vec2i;
typedef Vec<float, 4> Vec4f;
typedef Vec<double, 3> Vec3d;


// 构建多通道mat对象
Mat mm = (Mat_<Vec3f>(2, 2)<<Vec3f(1, 2 3), Vec3f(4, 5, 6), Vec3f(7, 8, 9), Vec3f(10, 11, 12));
for (int r = 0; r < mm.rows; ++r) {
	for (int c = 0; c < mm.cols; ++c) {
		cout << mm.at<Vec3f>(r, c) << ", "; // [1, 2, 3],...
	}
}



// 分离通道
vector<Mat> planes;
split(mm, planes);


// 合并通道
// p34
// 单通道合并为三通道
vector<Mat> plane;
plane.push_back(plane_0);
plane.push_back(plane_1);
plane.push_back(plane_2);
Mat mat;
merge(plane, mat);

// 获得Mat中某一区域
int r = 1, c = 0;
Mat mr = m.row(r);
Mat mc = m.row(c);

Range(int _start, int _end); // 左闭右开, 返回序列
Mat m_rrange = m.rowRange(Range(2, 4));
Mat m_crange = m.colRange(Range(2, 4));

// 克隆
Mat m_clone = m.rowRange(2, 4).clone(); 

// Rect类, 返回的矩阵指向原矩阵
Mat roi_1 = m(Rect(Point(2, 1), Point(3, 2))); // 左上角的坐标右下角的坐标
Mat roi_2 = m(Rect(2, 1, 2, 2)); // x, y, 宽度, 高度
Mat roi_3 = m(Rect(Point(2, 1), Size(2, 2))); //左上角的坐标, 尺寸


