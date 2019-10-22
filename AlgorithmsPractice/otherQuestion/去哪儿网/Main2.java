import java.util.*;
import java.io.*;
/* 
给出一个二叉树的中序遍历和后序遍历结果，求前序遍历结果输出

输入
第一行：中序遍历结果

第二行：后续遍历结果

输出
前序遍历结果


样例输入
dgbaechf 
gbdehfca
样例输出
adbgcefh
*/
// ac 100%
class TreeNode {
    char val;
    TreeNode left = null;
    TreeNode right = null;
    TreeNode(char x) { this.val = x;}
}
public class Main2 {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            String inorder = cin.nextLine();
            String postOrder = cin.nextLine();
            TreeNode root = buildTree(inorder.toCharArray(), postOrder.toCharArray());
            List<Character> list = new LinkedList<>();
            preOrder(root, list);
            printList(list);
        }
    }
    public static TreeNode buildTree(char[] inorder, char[] postorder) {
        int inLens = inorder.length;
        int posLens = postorder.length;

        return buildTree(inorder, 0, inLens-1, postorder, 0, posLens-1); 
    }

    public static TreeNode buildTree(char[] in, int inStart, int inEnd, char[] pos, int poStart, int poEnd) {
        if (inStart > inEnd || poStart > poEnd) {
            return null;
        }

        char rootValue = pos[poEnd];
        int rootIndex = 0;
        for (int i = 0; i <= inEnd; i++) {
            if (in[i] == rootValue) {
                rootIndex = i;
                break;
            }
        }

        int lens = rootIndex - inStart;
        TreeNode root = new TreeNode(rootValue);
        root.left = buildTree(in, inStart, rootIndex-1, pos, poStart, poStart+lens-1); 
        root.right = buildTree(in, rootIndex+1, inEnd, pos, poStart+lens, poEnd-1);

        return root;
    }

    public static void preOrder(TreeNode root, List<Character> list) {
        if (root != null) {
            list.add(root.val);
            preOrder(root.left, list);
            preOrder(root.right, list);
        }
    }

    public static void printList(List<Character> list) {
        StringBuilder sb = new StringBuilder();
        for (char c : list) {
            sb.append(c);
        }
        System.out.println(sb.toString());
    }
}