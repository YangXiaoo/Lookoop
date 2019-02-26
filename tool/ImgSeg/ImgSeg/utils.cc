// utils.cc
// 常用工具
#include <vector>
#include <string>

#include "utils.h"

using namespace std;

/* 生成序列 */
void gen_range(vector<int> &container, int low, int high, int gap, int max_gen) {
    int gen_counter = 0;
    while (low < high && gen_counter < max_gen) {
        if (gap > 0) {
            container.push_back(low);
            low += gap;
        } else {
            container.push_back(high);
            high += gap;
        }
        gen_counter += 1;

    } 
}