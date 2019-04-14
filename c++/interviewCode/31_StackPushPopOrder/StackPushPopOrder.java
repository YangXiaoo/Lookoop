// 2019-4-14

import java.util.*;

public class StackPushPopOrder {
	private List<Integer> list;
	public StackPushPopOrder(List<Integer> list) {
		this.list = list;
	}
	// 默认构造
	public StackPushPopOrder() {
	}

	// 是否为栈的弹出序列
	public boolean isPopOrder(List<Integer> order) {

		if (order.size() != list.size()) 
			return false;

		Stack<Integer> stack = new Stack<>();	// 定义辅助栈
		boolean ret = true;
		int start = 0;
		int idx = 0;
		int listSize = list.size();

		while (idx < listSize) {
			int tmpIndex = list.indexOf(order.get(idx));
			if (tmpIndex == -1) {
				ret = false;
				break;
			}

			// 将数据压入验证栈
			for (; start <= tmpIndex; ++start) {
				stack.push(list.get(start));
			}

			if (stack.peek() != order.get(idx)) {
				ret = false;
				break;
			}


			stack.pop();
			++idx;
		}

		return ret;

	}

	// 测试
	public void test(String testName, Integer[] _order) {
		List<Integer> order = Arrays.asList(_order);

		boolean ret = isPopOrder(order);

		System.out.println(testName + "result: " + ret);
	}


	public static void main(String[] args) {
		List<Integer> list = Arrays.asList(1,2,3,4,5);
		StackPushPopOrder test = new StackPushPopOrder(list);
		Integer[] order1 = {4,5,3,2,1};
		test.test("test1", order1);
		Integer[] order2 = {4, 3, 5, 1, 2};
		test.test("test2", order2);
	}
}