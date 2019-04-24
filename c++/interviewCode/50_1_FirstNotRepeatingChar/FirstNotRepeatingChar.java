// 2019-4-23
// 字符串中第一个只出现一次的字符

import java.util.*;

public class FirstNotRepeatingChar {
	public char getChar(String str) {
		HashMap<Character,Integer> map = new HashMap<>();
		for (int i = 0; i < str.length(); ++i) {
			if (!map.containsKey(str.charAt(i))) {
				map.put(str.charAt(i), 1);
			} else {
				map.put(str.charAt(i), map.get(str.charAt(i)) + 1);
			}
		}

		// System.out.println(map.toString());

		// 获取第一个值为1的key
		char ret = '0';
		for (int j = 0; j < str.length(); ++j) {
			char curKey = str.charAt(j);
			int curValue = map.get(curKey);
			if (curValue == 1) {
				ret = curKey;
				break;
			}
		}

		return ret;
	}

	// TreeMap根据插入顺序自动排序
	public char getCharUsingTreeMap(String str) {
		TreeMap<Character,Integer> map = new TreeMap<>();
		for (int i = 0; i < str.length(); ++i) {
			if (!map.containsKey(str.charAt(i))) {
				map.put(str.charAt(i), 1);
			} else {
				map.put(str.charAt(i), map.get(str.charAt(i)) + 1);
			}
		}

		// System.out.println(map.toString());
		// 获取第一个值为1的key
		char ret = '0';
		for (Map.Entry<Character, Integer> entry : map.entrySet()) {
			if (entry.getValue() == 1) {
				ret = entry.getKey();
				break;
			}
		}

		return ret;
	}

	public void test(String testName, String string, char expect) {
		// char ret = getChar(string);
		char ret = getCharUsingTreeMap(string);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		FirstNotRepeatingChar test = new FirstNotRepeatingChar();
		test.test("test1", "abaccdeff", 'b');
		test.test("test2", "abbsdsaccdeffpoiuy", 'e');
	}
}