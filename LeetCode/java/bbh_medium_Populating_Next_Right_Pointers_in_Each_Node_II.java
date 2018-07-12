/**

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
*/

// 2018-7-12
// 117. Populating Next Right Pointers in Each Node II


// Definition for binary tree with next pointer.
public class TreeLinkNode {
    int val;
    TreeLinkNode left, right, next;
    TreeLinkNode(int x) { val = x; }
}
public class bbh_medium_Populating_Next_Right_Pointers_in_Each_Node_II {
    public void connect(TreeLinkNode root) {
        if (root == null)
            return;
            
        TreeLinkNode cur = root;
        TreeLinkNode q = null;
        TreeLinkNode nextNode = null;
        
        while (cur != null) {
            if (cur.left != null) {
                if (q != null)
                    q.next = cur.left;                
                q = cur.left;
                if (nextNode == null)
                    nextNode = q;
            }
            
            if (cur.right != null) {
                if (q != null)
                    q.next = cur.right;
                q = cur.right;
                if (nextNode == null)
                    nextNode = q;
            }
            
            cur = cur.next;
        }
        
        connect(nextNode);
    }
}