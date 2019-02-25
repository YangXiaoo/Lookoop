// utils.cc
// 常用工具
#include <vector>
#include <string>

using namespace std;


/* 生成序列 */
template <typename _Ty>
vector<_Ty> gen_range(_Ty low, _Ty high, int gap, int max_gen) {
    vector<_Ty> container;
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
    return container;
}