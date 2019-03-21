// 2019-3-21
#include <stdio.h>
#include <vector>
#include <cstdio>
using namespace std;

/**
 * 重建二叉树
 * 根据前序遍历序列与中序遍历序列重构二叉树
 */


 /* 定义树节点 */
struct TreeNode
{
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int _val, TreeNode* _left = nullptr, TreeNode* _right = nullptr)
		: val(_val), left(_left), right(_right) {}
};


/* 递归辅助函数 */
TreeNode* helper(vector<int>& preorder, int p_start, int p_end,
	vector<int>& inorder, int i_start, int i_end);


/* 重建二叉树主函数 */
TreeNode* construct(vector<int>& preorder, vector<int>& inorder) {
	return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
}


/* 递归辅助函数 */
TreeNode* helper(vector<int>& preorder, int p_start, int p_end,
	vector<int>& inorder, int i_start, int i_end)
{
	if (p_start > p_end || i_start > i_end) return nullptr;

	int root_val = preorder[p_start];	// 获得根节点值
	int r_inorder_index;				// 根节点在中序序列中的索引
	for (int i = 0; i != inorder.size(); ++i)
		if (root_val == inorder[i])
			r_inorder_index = i;

	int lens = r_inorder_index - i_start;
	TreeNode* p_root = new TreeNode(root_val);
	p_root->left = helper(preorder, p_start + 1, p_start + lens, 
						  inorder, i_start, r_inorder_index - 1);
	p_root->right = helper(preorder, p_start + lens + 1, p_end, 
						   inorder, r_inorder_index + 1, i_end);

	return p_root;
}


/* 前序遍历打印 */
void print_preorder(const TreeNode* root) {
	if (root != nullptr) {
		printf("%d\t", root->val);
		print_preorder(root->left);
		print_preorder(root->right);
	}
}

/* 中序遍历打印 */
void print_inorder(const TreeNode* root) {
	if (root != nullptr) {
		print_inorder(root->left);
		printf("%d\t", root->val);
		print_inorder(root->right);
	}
}


int main(int argc, char const *argv[])
{
	vector<int> preorder = { 1, 2, 4, 7, 3, 5, 6, 8 };
	vector<int> inorder = { 4, 7, 2, 1, 5, 3, 8, 6 };

	TreeNode* root = construct(preorder, inorder);
	printf("前序遍历打印\n");
	print_preorder(root);	// 前序遍历打印

	printf("\n中序遍历打印\n");
	print_inorder(root);	// 中序遍历打印
	return 0;
}

// print:
// 前序遍历打印
// 1       2       4       7       3       5       6       8
// 中序遍历打印
// 4       7       2       1       5       3       8       6