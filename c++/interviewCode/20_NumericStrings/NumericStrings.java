// 2019-5-14


public class NumericStrings {
	private int index = 0;

	public boolean isNumeric(String str) {
		index = 0;	// 记录当前检测的索引位置
		int lenStr = str.length();
		boolean numeric = scanInteger(str);
		if ((index < str.length()) && (str.charAt(index) == '.')) {
			index++;
			numeric = scanUnsignInteger(str) || numeric;
		}

		if ((index < str.length()) && ((str.charAt(index) == 'e') || (str.charAt(index) == 'E'))) {
			index++;
			numeric = numeric && scanInteger(str);
		}
		// System.out.println(lenStr + ", " + index);
		return numeric && (lenStr == index);
	}


	public boolean scanInteger(String str) {
		if ((str.charAt(index) == '-') || (str.charAt(index) == '+')) {
			index++;
		}

		return scanUnsignInteger(str);
	}


	public boolean scanUnsignInteger(String str) {
		int before = index;
		while ((index < str.length()) && (str.charAt(index) >= '0') && (str.charAt(index) <= '9')) {
			index++;
		}

		return index > before;
	}

	public void test(String testName, String str, boolean expect) {
		boolean ret = isNumeric(str);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		NumericStrings test = new NumericStrings();

		String testStr1 = "+3.1416";
		String testStr2 = "-1E-16";
		String testStr3 = "-12e+4.5";
		test.test("test-1", testStr1, true);
		test.test("test-2", testStr2, true);
		test.test("test-3", testStr3, false);

	}
}

// test-1, expect: true, result: true
// test-2, expect: true, result: true
// test-3, expect: false, result: false