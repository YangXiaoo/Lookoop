// 2019-3-21
#include <stdio.h>
#include <vector>
#include <cstdio>
using namespace std;


/**
 * 二叉树的下一个节点
 * 给定一个二叉树和其中的一个节点，找出中序遍历序列的下一个节点。
 * 树中有两个分别指向左，右节点的指针，还有一个指向父节点的指针。
 */


 /* 定义树节点 */
struct TreeNode
{
	int val;
	TreeNode* parent;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int _val, TreeNode* _parent=nullptr, TreeNode* _left = nullptr, 
			 TreeNode* _right = nullptr)
			 : val(_val), parent(_parent), left(_left), right(_right) {}
};


/**
 * 情况分为：
 * 树节点有右孩子
 * 树节点无右孩子，查看父亲，如果有父亲且为父亲的左孩子则为下一个遍历节点
 */
TreeNode* nextNode(TreeNode* node) {
	// 特殊情况判断
	if (node == nullptr) return nullptr;

	TreeNode* next = nullptr;
	TreeNode* n_right = node->right;

	// 如果有右孩子
	if (n_right != nullptr) {
		next = n_right;
		while (next->left != nullptr) {
			next = next->left;
		}
	} else if (node->parent != nullptr) {
		TreeNode* p = node->parent;
		TreeNode* cur = node;

		while (p != nullptr && cur == p->right) {
			cur = p;
			p = p->parent;
		}

		next = p;
	}

	return next;
}

void construct(TreeNode* root, TreeNode* left, TreeNode* right) {
	root->left = left;
	if (left)
		left->parent = root;

	root->right = right;
	if (right)
		right->parent = root;
} 

// 树结构

// 	      1
// 	    /   \
// 	   /     \
// 	  2       3
// 	 / \	 / \
// 	4	5	6	7
// 	   / \
// 	  8   9

void test(const char* call_name, TreeNode* node, TreeNode* expect) {
	printf("call test name  %s, result: ", call_name);

	TreeNode* next = nextNode(node);
	if (expect == next) 
		printf("passed.\n");
	else
		printf("failed.\n");
}



int main(int argc, char const *argv[])
{
	TreeNode* node1 = new TreeNode(1);
	TreeNode* node2 = new TreeNode(2);
	TreeNode* node3 = new TreeNode(3);
	TreeNode* node4 = new TreeNode(4);
	TreeNode* node5 = new TreeNode(5);
	TreeNode* node6 = new TreeNode(6);
	TreeNode* node7 = new TreeNode(7);
	TreeNode* node8 = new TreeNode(8);
	TreeNode* node9 = new TreeNode(9);

	construct(node1, node2, node3);
	construct(node2, node4, node5);
	construct(node5, node8, node9);
	construct(node3, node6, node7);

	test("test1", node1, node6);	// passed
	test("test2", node4, node8);	// failed
	test("test3", node9, node1);	// passed
	test("test4", node7, nullptr);	// passed
	test("test5", node2, node8);	// passed

	return 0;
}

// print:
// call test name  test1, result: passed.
// call test name  test2, result: failed.
// call test name  test3, result: passed.
// call test name  test4, result: passed.
// call test name  test5, result: passed.