// 2020-3-24
// java实现排序
// 快排，归并，插入，冒泡，选择排序, 计数排序，桶排序
import java.util.*;

public class javaSort {
	public static int REVERSED = -1;
	public static int SORTED = 1;
	// 交换数组工具
	public static void swap(int[] nums, int index1, int index2) {
		int tmp = nums[index1];
		nums[index1] = nums[index2];
		nums[index2] = tmp;
	}

	// 打印数组
	public static void print(int[] nums) {
		System.out.println(Arrays.toString(nums));
	}

	// 外接口
	// 快排
	public void qucikSort(int[] nums) {
		new QuickSort().sort(nums);
	}
	// 归并
	public void mergeSort(int[] nums) {
		new MergeSort().sort(nums);
	}

	// 快排
	class QuickSort {
		// 快排入口函数
		public void sort(int[] nums) {
			int right = nums.length - 1;
			sortHelper(nums, 0, right);
			print(nums);
		}

		public void sort(int[] nums, int left, int right) {
			sortHelper(nums, left, right);
			print(nums);
		}

		// 找到基准点
		public int findPivot(int[] nums, int left, int right) {
			int midIndex = (left + right) >> 1;
			// 交换中间点与末尾点
			swap(nums, midIndex, right);

			// 小于末尾的放到前面去
			int start = left;
			for (int i = left; i < right; i++) {
				if (nums[i] < nums[right]) {
					swap(nums, i, start);
					start++;
				}
			}

			swap(nums, start, right);

			return start;
		}

		// 排序辅助函数
		public void sortHelper(int[] nums, int left, int right) {
			if (left < right) {
				int pivotIndex = findPivot(nums, left, right);
				sortHelper(nums, left, pivotIndex-1);
				sortHelper(nums, pivotIndex+1, right);
			}
		}
	}

	// 归并排序类
	class MergeSort {
		public void sort(int[] nums) {
			int left = 0, right = nums.length;
			sortHelper(nums, left, right-1);
			print(nums);
		}

		public void sortHelper(int[] nums, int left, int right) {
			if (left < right) {
				int mid = (left + right) >> 1;
				sortHelper(nums, left, mid);
				sortHelper(nums, mid + 1, right);
				merge(nums, left, mid, right);
			}
		}

		public void merge(int[] nums, int left, int mid, int right) {
			int length = right - left + 1;
			int[] tmp = new int[length];
			int i = left, j = mid + 1, index = 0;

			// 先将两部分数据按大小放入tmp数组中
			while (i <= mid && j <= right) {
				if (nums[i] < nums[j]) {
					tmp[index++] = nums[i++];
				} else {
					tmp[index++] = nums[j++];
				}
			}

			// 将两部分数据剩下的数据放入tmp中
			while (i <= mid) {
				tmp[index++] = nums[i++];
			}

			while (j <= right) {
				tmp[index++] = nums[j++];
			}

			// 将排序好的数据放入原数组中
			for (int k = 0; k < length; ++k) {
				nums[left+ k] = tmp[k];
			}
		}
	}


	// 选择排序
	public void selectSort(int[] nums) {
		int length = nums.length;
		for (int i = 0; i < length - 1; ++i) {
			for (int j = i + 1; j < length; ++j) {
				if (nums[i] > nums[j]) {
					swap(nums, i, j);
				}
			}
		}

		print(nums);
	}

	public void selectSort(int[] nums, int sortCode) {
		int length = nums.length;
		for (int i = 0; i < length - 1; ++i) {
			for (int j = i + 1; j < length; ++j) {
				if (nums[i] < nums[j] && sortCode == REVERSED) {
					swap(nums, i, j);
				} else if (nums[i] > nums[j] && sortCode == SORTED) {
					swap(nums, i, j);
				}
			}
		}

		print(nums);
	}


	public static void main(String[] args) {
		// test
		int[] nums = {3, 4, 1, 6, 2, 9, 11, 5, 878, 234, 3};
		javaSort util = new javaSort();
		util.qucikSort(nums);
		util.mergeSort(nums);
		util.selectSort(nums, javaSort.REVERSED);
	}

}