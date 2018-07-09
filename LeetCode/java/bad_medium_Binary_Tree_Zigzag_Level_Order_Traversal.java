/**
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
*/


// 103
// 2018-7-9
// bad_Binary_Tree_Zigzag_Level_Order_Traversal

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bad_medium_Binary_Tree_Zigzag_Level_Order_Traversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    	// res： 输出
    	// treenode: 存储每一层所有节点
        List<List<Integer>> res = new ArrayList<>();
        Deque<TreeNode> treenode = new LinkedList<>();

        if (root == null) {
        	return res;
        } else {
        	List<Integer> tmp = new ArrayList<>();
        	tmp.add(root.val);
        	treenode.push(root); // 向头部插入一个元素，插入失败报错
        	res.add(tmp);
        }

        int queue = 1;
        while (!treenode.isEmpty()) {
        	int i = treenode.size();
        	List<Integer> tmpRes = new ArrayList<>();

        	while (i > 0) {
        		if (queue % 2 == 1) {
        			TreeNode node = treenode.pollLast(); // 弹出列队尾部元素，失败返回null
	        		if (node.right != null) {
	        			tmpRes.add(node.right.val);
	        			treenode.offerFirst(node.right); // 在列队头部插入元素，失败返回false
	        		}
	        		if (node.left != null) {
	        			tmpRes.add(node.left.val);
	        			treenode.offerFirst(node.left);
	        		} 
        		} else {
        			TreeNode node = treenode.pollFirst(); // 弹出列队头部元素，失败返回null
	        		if (node.left != null) {
	        			tmpRes.add(node.left.val);
	        			treenode.offerLast(node.left); // 在列队尾部插入元素，失败返回false
	        		} 
	        		if (node.right != null) {
	        			tmpRes.add(node.right.val);
	        			treenode.offerLast(node.right);
	        		}
        		}

        		i--;
        	}

        	queue++;
        	if (!tmpRes.isEmpty()) res.add(tmpRes);
        }

        return res;
    }
}