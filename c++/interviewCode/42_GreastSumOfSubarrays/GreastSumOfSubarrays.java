// 2019-4-22
// 连续子数组的最大和
// letcode-54

public class GreastSumOfSubarrays {
	public int getGreast(int[] nums) {
		if (nums.length == 0) return -1;

		int max = nums[0];

		for (int i = 1; i < nums.length; ++i) {
			if (nums[i - 1] > 0) {
				nums[i] += nums[i - 1];
				if (nums[i] > max) {
					max = nums[i];
				}
			}
		}

		return max;
	}

	public void test(String testName, int[] nums, int expect) {
		int max = getGreast(nums);
		System.out.println(testName + ", expect: " + expect + ", result: " + max);
	}

	public static void main(String[] args) {
		GreastSumOfSubarrays test = new GreastSumOfSubarrays();
		int[] nums1 = {1,-2,3,10,-4,7,2,-5};
		test.test("test1", nums1, 18);
	}
}