// utils.h
// 常用工具

#include <vector>

/* 生成序列 */
template <typename _Ty>
std::vector<_Ty> gen_range(_Ty low, _Ty high, int gap, int max_gen);