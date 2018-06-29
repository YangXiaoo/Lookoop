"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# 2018-6-29
# Unique Binary Search Tree II
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate(1,n)

    def generate(self,start,end):
        if start > end:
            return [None]
        if start == end:
            node = TreeNode(start)
            return [node]
        res = []
        for i in range(start,end+1):
            l = self.generate(start,i-1)
            r = self.generate(i+1,end)
            #print(l,r)
            for m in l:
                for n in r:
                    root = TreeNode(i)
                    root.left = m
                    root.right = n
                    res.append(root)


        return res

class Print:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return 
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)

        return self.res
        
# test
n = 3
test = Solution()
res = test.generateTrees(n)

prints = Print()
for i in res:
    r = prints.inorderTraversal(i)
    print(r)




"""class Solution {
public:
 
    vector<TreeNode*> generateTrees(int n) {
        return generateTrees1(1,n);
    }
    
    vector<TreeNode*> generateTrees1(int start, int end){
        if(start>end){
            vector<TreeNode*> res_vec;
            res_vec.push_back(NULL);
            return res_vec;
        }
        else if(start==end){
            vector<TreeNode*> res_vec;
            TreeNode* res_node=new TreeNode(start);
            res_vec.push_back(res_node);
            return res_vec;
        }
        
        vector<TreeNode*> res_vec;
        for(int i=start;i<=end;i++){
            vector<TreeNode*> l_vec=generateTrees1(start, i-1);
            vector<TreeNode*> r_vec=generateTrees1(i+1,end);
            for(int k=0;k<l_vec.size();k++){
                for(int j=0;j<r_vec.size();j++){
                    TreeNode* root=new TreeNode(i);
                    root->left=l_vec[k];
                    root->right=r_vec[j];
                    res_vec.push_back(root);
                }
            }
        }
        return res_vec;
"""