/**
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*/

// 2018-7-10
// 109. Convert Sorted List to Binary Search Tree

//Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
     ListNode(int x) { val = x; }

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class baj_Convert_Sorted_List_to_Binary_Search_Tree {
    public TreeNode sortedListToBST(ListNode head) {
        ListNode node = head;
        List<Integer> nums = new ArrayList<Integer>();
        while (node != null) {
            nums.add(node.val);
            node = node.next;
        }

        return buildTree(nums, 0, nums.length-1);
    }

    public TreeNode buildTree(int[] nums, int low, int hight) {
        // 使用递归添加节点
        if (low > hight) {
            return null;
        }

        int mid = (low + hight) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = buildTree(nums, low, mid-1);
        root.right = buildTree(nums, mid+1, hight);

        return root;
    }
}

public class Solution {
    static ListNode currentHead = null;
    TreeNode buildTree(int start, int end) {
        if(start>end) {
            return null;
        }
        int mid = start + (end - start)/2;
        TreeNode left = buildTree(start, mid-1);
        TreeNode root = new TreeNode(currentHead.val);
        root.left = left;
        currentHead = currentHead.next;
        root.right = buildTree(mid + 1, end);
        return root;
    }
    
    public TreeNode sortedListToBST(ListNode head) {
        if(head==null) {
            return null;
        }
        currentHead = head;
        int len = 0;
        while(head!=null) {
            len++;
            head = head.next;
        }
        
        return buildTree(0, len-1);
    }
}
