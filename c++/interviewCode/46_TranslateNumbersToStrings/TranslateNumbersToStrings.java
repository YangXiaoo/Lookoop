// 2019-4-22
// letcode-91
// 把数字翻译成字符串
// 给定一个数字，按照规律：0翻译为"a", 1翻译为"b",...,25翻译为"z"。
// 一个数字可能有多个翻译，例如，12258有5中不同翻译"bccfi", "bwfi", "bczi", "mcfi","mzi"。

public class TranslateNumbersToStrings {
	public int numbersToString(long numbers) {
		String numbersInString = String.valueOf(numbers);

		if (numbersInString.length() == 1) return 1;
		System.out.println("numbersInString: " + numbersInString);

		int[] dp = new int[numbersInString.length() + 1];

		dp[0] = 1;
		dp[1] = 1;
		for (int i = 1; i < numbersInString.length(); ++i) {
			dp[i+1] += dp[i];

			// 测试
			System.out.println((numbersInString.charAt(i-1) - '0') + ", " + ((numbersInString.charAt(i-1) - '0')*10 + (numbersInString.charAt(i) - '0')));

			if (((numbersInString.charAt(i-1) - '0') != 0) 
				&& (((numbersInString.charAt(i-1) - '0')*10 + (numbersInString.charAt(i) - '0')) <= 25)) {
				dp[i+1] += dp[i-1];
			}
		}

		return dp[dp.length-1];
	}

	public void test(String testName, long numbers, int expect) {
		int ret = numbersToString(numbers);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		TranslateNumbersToStrings test = new TranslateNumbersToStrings();

		long numbers = 12258;
		test.test("test1", numbers, 5);
	}
}

// numbersInString: 12258
// 1, 12
// 2, 22
// 2, 25
// 5, 58
// test1, expect: 5, result: 5