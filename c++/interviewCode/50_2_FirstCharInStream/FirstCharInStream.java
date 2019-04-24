// 2019-4-23
// 字符流中第一个只出现一次的字符

import java.util.*;

public class FirstCharInStream {
	private int[] record = new int[256];
	private int index;

	// 初始化
	public FirstCharInStream() {
		Arrays.fill(record, -1);
	}

	public void insert(char c) {
		int value = Integer.valueOf(c);
		if (record[value] == -1) 
			record[value] = index;
		else
			record[value] = -2;
		++index;
	}

	public char firstAppearing() {
		// record中大于-1的并且值最小的索引
		int minValue = index;
		int minIndex = 0;
		for (int i = 0; i < record.length; ++i) {
			if ((record[i] > -1) && (record[i] < minValue)) {
				minValue = record[i];
				minIndex = i;
			}
		}

		return (char)minIndex;
	}


	public void test(String testName, char c, char expect) {
		insert(c);
		char ret = firstAppearing();

		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		FirstCharInStream test = new FirstCharInStream();
		test.test("test1", 'g', 'g');
		test.test("test2", 'o', 'g');
		test.test("test3", 'o', 'g');
		test.test("test4", 'g', ' ');
		test.test("test5", 'l', 'l');
		test.test("test6", 'e', 'e');
	}
}

// test1, expect: g, result: g
// test2, expect: g, result: g
// test3, expect: g, result: g
// test4, expect:  , result:
// test5, expect: l, result: l
// test6, expect: e, result: l