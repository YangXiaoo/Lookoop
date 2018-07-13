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
            
        TreeLinkNode cur = root; // 记录每一层的根节点
        TreeLinkNode q = null; // 接头
        TreeLinkNode nextNode = null; //记录每一层节点下一层的孩子，以此来遍历所有节点
        
        while (cur != null) {
            if (cur.left != null) {
                if (q != null)  // 如果根节点左边根节点的孩子q存在则将当前根节点的左子树cur.left与q连接
                    q.next = cur.left;               
                q = cur.left;  // 改变接头 
                if (nextNode == null) // 当前节点层遍历完后，下一层从nextNode节点开始遍历，只记录一次。
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
    //对列
    /*
    public void connect(TreeLinkNode root) {
        Queue<TreeLinkNode> cur_layer = new LinkedList<>();
        Queue<TreeLinkNode>  next_layer = new LinkedList<>();
        TreeLinkNode cur_node;
        TreeLinkNode next_node;
        int cur_index = 0;
        if(root!=null) cur_layer.add(root);
    
        while(!cur_layer.isEmpty()){
            cur_node = cur_layer.poll();
            if(cur_node.left != null) next_layer.add(cur_node.left);
            if(cur_node.right != null) next_layer.add(cur_node.right);
            while(!cur_layer.isEmpty()){
                next_node = cur_layer.poll();
                cur_node.next = next_node;
                cur_node = next_node;
                if(cur_node.left != null) next_layer.add(cur_node.left);
                if(cur_node.right != null) next_layer.add(cur_node.right);
            }
            cur_node.next = null;
            Queue<TreeLinkNode> tmp = cur_layer;
            tmp = cur_layer;
            cur_layer = next_layer;
            next_layer = tmp;
        }
        
    }*/