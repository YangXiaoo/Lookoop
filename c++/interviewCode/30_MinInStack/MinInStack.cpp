// 2019-3-30
#include <stdio.h>
#include <stack>
#include <assert.h>
using namespace std;

/**
 * 定义栈的数据结构
 * 在该类型中实现一个能够得到栈的最小元素min函数, 调用min, push, pop
 * 的时间复杂度都是O(1)
 */

template <typename T>
class StackWithMin {
 public:
 	StackWithMin() {}
 	virtual ~StackWithMin() {}

 	T& top();
 	const T& top() const;

 	void push(const T& value);
 	void pop();

 	const T& min() const;

 	bool empty() const;
 	size_t size() const;

 private:
 	stack<T> m_data;
 	stack<T> m_min;
}

template <typename T>
void StackWithMin::push(const T& value) {
	m_data.push(value);

	if (m_min.size() == 0 || value < m_min.top())
		m_min.push(value);
	else
		m_min.push(m_min.top());
}


template <typename T> 
void StackWithMin<T>::pop() {
	assert(m_min.size() > 0 && m_data.size() > 0);

	m_min.pop();
	m_data.pop();
}

template <typename T> 
const T& StackWithMin<T>::min() const {
	assert(m_min.size() > 0 && m_data.size() > 0);

	return m_min.top();
}

template <typename T> 
T& StackWithMin<T>::top() {
    return m_data.top();
}

template <typename T> 
const T& StackWithMin<T>::top() const {
    return m_data.top();
}

template <typename T> 
bool StackWithMin<T>::empty() const {
    return m_data.empty();
}

template <typename T> 
size_t StackWithMin<T>::size() const {
    return m_data.size();
}