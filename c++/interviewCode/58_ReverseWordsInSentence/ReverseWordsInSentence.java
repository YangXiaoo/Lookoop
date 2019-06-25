// 2019-4-25
// 翻转字符串
// leetcode-151

import java.util.*;

public class ReverseWordsInSentence {
	public String reverse(String str) {
		char[] charArray = str.toCharArray();	// 转换为数组

		// 整个字符串翻转
		int start = 0, end = charArray.length - 1;
		while (start < end) {
			char tmp = charArray[start];
			charArray[start] = charArray[end];
			charArray[end] = tmp;

			start++;
			end--;
		}
		System.out.println("reverse sentence: " + Arrays.toString(charArray));
		// 单个字符串翻转
		// 有错
		// boolean flag = false;
		// int left = 0;
		// for (int i = 0; i < charArray.length; ++i) {
		// 	if (!flag) {
		// 		if (charArray[i] != ' ') {
		// 			left = i;
		// 			flag = true;
		// 			continue;
		// 		}
		// 	}

		// 	if ((charArray[i] == ' ')) {
		// 		swapRange(charArray, left, i - 1);
		// 		flag = false;
		// 	}

		// 	if ((i == charArray.length - 1) && flag) {
		// 		swapRange(charArray, left, i);
		// 	}
		// }

		int left = 0;	// 记录左端索引
		boolean canSwap = false;
		for (int i = 0; i < charArray.length; ++i) {
			if (charArray[i] == ' ') {
				if (canSwap) {
					swapRange(charArray, left, i - 1);
					canSwap = false;
				}
				left = i + 1;
			} else {
				canSwap = true;
			}

			if (i == charArray.length - 1 && canSwap) {
				swapRange(charArray, left, i);
			}
		}

		return new String(charArray);
	}

	public void swapRange(char[] array, int left, int right) {
		while (left < right) {
			char tmp = array[left];
			array[left] = array[right];
			array[right] = tmp;

			left++;
			right--;
		}
	}

	public void test(String testName, String str, String expect) {
		String ret = reverse(str);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret + ".");
	}

	public static void main(String[] args) {
		ReverseWordsInSentence test = new ReverseWordsInSentence();
		test.test("test-1", "i  am a  student.", "student.  a am  i");
		test.test("test-1", " i  am a  student. ", " student.  a am  i ");
	}
}