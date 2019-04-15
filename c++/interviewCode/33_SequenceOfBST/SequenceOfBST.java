// 2019-4-14
// 输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历结果。
import java.util.*;

public class SequenceOfBST {
	// private Integer[] sequence;
	// public SequenceOfBST(Integer[] sequence) {
	// 	this.sequence = sequence;
	// }

	public boolean VerifySequenceOfBST(Integer[] sequence) {
		if (sequence.length == 0)
			return true;

		int root = sequence[sequence.length-1];
		int leftIndex = 0;
		// 找出左子树
		for (int i = 0; i < sequence.length; ++i) {
			if (sequence[i] > root) {
				leftIndex = i;
				break;
			}
		}

		boolean left = true;
		if (leftIndex > 0) 
			left = VerifySequenceOfBST(Arrays.copyOfRange(sequence, 0, leftIndex));

		int j = leftIndex;
		for (; j < sequence.length; ++j) {
			if (sequence[j] < root) 
				return false;
		}

		boolean right = true;
		if  (j < sequence.length - 1)
			right = VerifySequenceOfBST(Arrays.copyOfRange(sequence, leftIndex, sequence.length));

		return  (left && right);
	}

	public void test(String testName, Integer[] sequence) {
		boolean ret = VerifySequenceOfBST(sequence);
		System.out.println(testName+", result: " + ret);
	}

	public static void main(String[] args) {
			SequenceOfBST verify = new SequenceOfBST();
			Integer[] list1 = {5, 7, 6, 9, 11, 10, 8};
			verify.test("test1", list1);

			Integer[] list2 = {7, 4, 6, 5};
			verify.test("test2", list2);	
		}	
}