// 2019-4-21
// 获取数据流的中位数
// https://www.cnblogs.com/yongh/p/9944993.html

import java.util.PriorityQueue;
import java.util.Comparator;

public class StreamMedian {
	PriorityQueue<Integer> minStack = new PriorityQueue<>();
	PriorityQueue<Integer> maxStack = new PriorityQueue<>(10, new Comparator<Integer>(){
		public int compare(Integer val1, Integer val2) {
			return val2 - val1;
		}
	});

	// 偶数插入最小堆，奇数时插入最大堆
	public void insert(Integer num) {
		// 偶数时
		if (((minStack.size() + maxStack.size()) & 1) == 0) {
			// 如果插入最小堆的数比最大堆的数还小则将插入数先插入最大堆，
			// 将最大堆取出作为插入最小堆的数据
			if (!maxStack.isEmpty() && (maxStack.peek() > num)) {
				int tmp = maxStack.poll();
				maxStack.offer(num);
				num = tmp;
			}
			minStack.offer(num);
		} else {
			// 如果插入最大堆的数大于最小堆中的数则交换
			if (!minStack.isEmpty() && (minStack.peek() < num)) {
				int tmp = minStack.poll();
				minStack.offer(num);
				num = tmp;
			}
			maxStack.offer(num);
		}
	}

	public Double getMedian() {
		if ((minStack.size() + maxStack.size()) == 0) 
			throw new RuntimeException();

		double median;
		if (((maxStack.size() + minStack.size()) & 1) == 0) {
			median = (minStack.peek() + maxStack.peek()) / 2.0;
		} else {
			median = minStack.peek();
		}

		return median;
	}

	public void test(String testName, int num, double expect) {
		insert(num);
		double ret = getMedian();
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		StreamMedian test = new StreamMedian();
		test.test("test1", 1, 1.0);
		test.test("test2", 2, 1.5);
		test.test("test3", 3, 2.0);
		test.test("test4", 4, 2.5);
	}
} 

// test1, expect: 1.0, result: 1.0
// test2, expect: 1.5, result: 1.5
// test3, expect: 2.0, result: 2.0
// test4, expect: 2.5, result: 2.5