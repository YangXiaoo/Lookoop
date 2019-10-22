// 2019-4-23
// leetcode-34
// 数字在排序数组中出现的次数

public class NumberOfK {
	public int getCount(int[] nums, int target) {
		int left = getLeft(nums, target);
		int right = getRight(nums, target);

		return right - left + 1;
	}

	public int getLeft(int[] nums, int target) {
		int ret = 0;
		int start = 0, end = nums.length - 1;

		while ( (start >= 0) && (end < nums.length) && (end >= start)) {
			int mid = (start + end) >> 1;

			if (nums[mid] == target) {
				if (((mid > 0) && (nums[mid-1] != target)) || (mid == 0)) {
					ret = mid;
					break;
				} else {
					end = mid - 1;
				}
			}

			if (nums[mid] < target) 
				start = mid + 1;
			else if (nums[mid] > target)
				end = mid - 1;
		}

		return ret;
	}

	public int getRight(int[] nums, int target) {
		int ret = 0;
		int start = 0, end = nums.length - 1;

		while ( (start >= 0) && (end < nums.length) && (end >= start)) {

			int mid = (start + end) >> 1;

			if (nums[mid] == target) {
				if (((mid > 0) && (nums[mid+1] != target)) || (mid == nums.length - 1)) {
					ret = mid;
					break;
				} else {
					start = mid + 1;
				}
			}


			if (target > nums[mid]) 
				start = mid;
			else if (target < nums[mid])
				end = mid - 1;;
		}

		return ret;
	}

	public void test(String testName, int[] nums, int traget,  int expect) {
		int ret = getCount(nums, traget);

		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		NumberOfK test = new NumberOfK();

		int[] nums1 = {1,2,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,8};
		test.test("test-1", nums1, 3, 3);
		test.test("test-2", nums1, 2, 1);	
		test.test("test-3", nums1, 4, 7);
		test.test("test-4", nums1, 5, 6);
	}
}

// test-1, expect: 3, result: 3
// test-2, expect: 1, result: 1
// test-3, expect: 7, result: 7
// test-4, expect: 6, result: 6