// 2019-4-16
// 待验证, 与LeetCode 113,114相同
import java.util.*;

class TreeNode {
	int val;
	TreeNode left = null;
	TreeNode right = null;
}

public class PathInTree {
	List<List<Integer>> path = new LinkedList<LinkedList<>>();
	public List<List<TreeNode>> findPath(TreeNode root, Integer sum) {
		List<TreeNode> tmp = new LinkedList<>();
		helper(tmp, sum);
		return path;
	}

	public void helper(TreeNode root, List<TreeNode> tmp, Integer sum) {
		if (root == null):
			return ;

		if (root.left == null && root.right == null) {
			tmp.add(root.val);
			if (equal(tmp, sum)) {
				path.add(new LinkedList(tmp));
			}
			tmp.remove(tmp.size()-1);
		} else {
			tmp.add(root.val);
			helper(root.left, tmp, sum);
			helper(root.right, tmp, sum);
			tmp.remove(tmp.size()-1);
		}
	}

	public boolean equal(List<TreeNode> tmp, Integer sum) {
		int total = 0;
		for (Integer node : tmp) {
			total += node;
		}
		return total == sum;
	}
}