public class Main {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			int n = Integer.parseInt(cin.next());
			int nextLens = (int)Math.sqrt(2, n);
			for(int i = 0; i < ; ++i) {
				// 待做
			}
		}
	}

	public static int[] reverseGap(int[] nums, int gap) {
		int it = 0;
		for (int i = 0; i < nums.length; ++i) {
			if (it == gap) {
				reverseRange(nums, i - gap, i);
				it = 0;
			}
			++it;
		}
	}

	public static void reverseRange(int[] nums, int left, int right) {
		while (left <= right) {
			int tmp = nums[left];
			nums[left] = nums[right];
			nums[right] = tmp;
			left++;
			right--;
		}
	}

	public static int computePair(int[] nums) {
		int count = 0;
		for (int i = 0; i < nums.length-1; +=i) {
			for (int j = i; j < length; ++j) {
				if (nums[i] > nums[j]) {
					count++;
				}
			}
		}
	}
}