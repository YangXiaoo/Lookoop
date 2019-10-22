// 2019-4-23
// 数组中的逆序对
// 如, {7,5,6,4}， 一共存在5对逆序对: {7,6}, {7,5}, {7,4}, {6,4}. {5,4}

import java.util.*;

public class InversePair {
	// 采用归并方法
	public List<List<Integer>> inverse(Integer[] nums) {
		List<Integer> numsList = Arrays.asList(nums);
		List<List<Integer>> pair = new ArrayList<List<Integer>>();
		inverseHelper(numsList, pair);

		return pair;
	}

	public List<Integer> inverseHelper(List<Integer> nums, List<List<Integer>> pair) {
		if (nums.size() == 1)
			return nums;

		int mid = nums.size() >> 1;

		List<Integer> left = inverseHelper(new ArrayList(nums.subList(0, mid)), pair);
		List<Integer> right = inverseHelper(new ArrayList(nums.subList(mid, nums.size())), pair);

		List<Integer> ret = new LinkedList<>();
		while ((left.size() > 0) && (right.size() > 0)) {
			if (left.get(0) > right.get(0)) {
				for (Integer x : right) {
					List<Integer> tmpPair = new ArrayList<>();
					tmpPair.add(left.get(0));
					tmpPair.add(x);
					pair.addAll(new ArrayList(tmpPair));
					System.out.println("pair: " + tmpPair.toString());
				}
				ret.add(left.get(0));
				left.remove(0);
			} else {
				ret.add(right.get(0));
				right.remove(0);
			}
		}

		if (!left.isEmpty())
			ret.addAll(left);
		if (!right.isEmpty())
			ret.addAll(right);

		return ret;
	}

	public void test(String testName, Integer[] nums) {
		List<List<Integer>> ret = inverse(nums);
		System.out.println(testName + ", result: " + ret.toString());
	}

	public static void main(String[] args) {
		InversePair test = new InversePair();
		Integer[] nums = {7, 5, 6, 4};
		test.test("test1", nums);
	}
}

// pair: [7, 5]
// pair: [6, 4]
// pair: [7, 6]
// pair: [7, 4]
// pair: [5, 4]
// test1, result: [7, 5, 6, 4, 7, 6, 7, 4, 5, 4]