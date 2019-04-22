// 2019-4-22
// 数字序列中某一位的数字
// 数字以0123456789101112....的格式序列化得到一个字符序列中索引对应的数字, 如第13位为1.

public class DigitsInSequence {
	public int getDigit(int index) {
		int digit = 1;	// 记录当前的位数，从一位数开始

		while (true) {
			int number = getCount(digit);		// 获得当前位数占据字符序列的长度
			if (number > index) {
				return getNumber(digit, index);	// 获得结果
			}

			index -= digit * number;
			digit++;
		}
	}

	// 限定 digit >= 1
	public int getCount(int digit) {
		if (digit == 1) {
			return 10;
		}

		return 9*(int)Math.pow(10, digit-1);
	}

	public int getBase(int digit) {
		if (digit == 1) 
			return 0;
		return (int)Math.pow(10, digit);
	}

	public int getNumber(int digit, int index) {
		int num = getBase(digit) + index/digit;	// 获得当前数字
		int idx = digit - index % digit;		// 第Num个数字+idx位
		for (int i = 1; i < idx; ++i) {			// idx等于1时为最后一位
			num /= 10;
		}

		return num % 10;
	}

	public void test(String testName, int index, int expect) {
		int number = getDigit(index);
		System.out.println(testName + ", expect: " + expect + ", result: " + number);
	}

	public static void main(String[] args) {
		DigitsInSequence test = new DigitsInSequence();
		test.test("test1", 5, 5);
		test.test("test2", 13, 1);
		test.test("test3", 19, 4);
		test.test("test4", 1001, 7);
	}


// test1, expect: 5, result: 5
// test2, expect: 1, result: 1
// test3, expect: 4, result: 4
// test4, expect: 7, result: 7