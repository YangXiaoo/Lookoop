// 2019-2-18
// Sales_data.h

#ifndef SALES_DATA_H
#define SALES_DATA_H

#include <iostream>
#include <string>


class Sales_data {
private:
	std::string book_no;
	unsigined units_sold = 0;
	double revenue = 0.0;

public:
	Sales_data() = default; // 默认构造函数
	Sales_data(const std::string &s, unsigined n, double r) : 
			   book_no(s), units_sold(n), revenue(r * n) {}
	Sales_data(const std::string &s) : book_no(s) {}
	Sales_data(std::istream&);
	
	std::string is_bn() const { return book_no; }
	Sales_data &combine(const Sales_data&);

friend Sales_data add(const Sales_data&, const Sales_data&); // 友元函数可以访问私有变量
friend std::istream &read(std::istream&, Sales_data&);
friend std::ostream &print(std::ostream&, const Sales_data&);
}


// 非成员函数声明
Sales_data add(const Sales_data&, const Sales_data&);
std::istream &read(std::istream&, Sales_data&);
std::ostream &print(std::ostream&, const Sales_data&);

inline
bool sales_compare(const Sales_data &sales_a, const Sales_data &saleb) {
	return sales_a.is_bin() > sales_b.is_bin();
}

#endif