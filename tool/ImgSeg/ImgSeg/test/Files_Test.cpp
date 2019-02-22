// Files_Test.cpp
// 2019-2-22
#include <string>
#include <string>
#include <ostream>
#include "imgseg/util/Files.h"

using namespace std;

int main(int argc, char const *argv[])
{
	vector<string> suffix = {".png"};
	int model = 0;

	string file_path("xx");
	Files files(file_path, suffix, model);
	vector<string> files_list;

	files.get_files(files_list);

	cout << files_list << endl;
	return 0;
}