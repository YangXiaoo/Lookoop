// 2019-3-30
#include <stdio.h>
#include <vector>
using namespace std;

/* 输入两棵二叉树A,B, 判断B是不是A的子结构 */


/* float不能直接比较 */
bool equal(float val1, float val2) {
	if ((val1-val2) < 0.0000001 && (val1-val2) > -0.0000001)
		return true;
	else
		return false;
}

/* 辅助函数 */
bool hasSubTree(TreeNode* pHead1, TreeNode* pHead2) {
	if (pHead2 == nullptr)
		return true;
	if (pHead1 == nullptr)
		return false;

	if (!equal(pHead1->val, pHead2->val))
		return false;

	return hasSubTree(pHead1->left, pHead2->left) && hasSubTree(pHead1->right, pHead2->right);
}

bool isSubTree(TreeNode* pHead1, TreeNode* pHead2) {
	bool ret = false;
	if (pHead1 != nullptr && pHead2 != nullptr) {
		if (equal(pHead1->val, pHead2->val)) {
			ret = hasSubTree(pHead1, pHead2);
		}

		if (!ret) {
			ret = hasSubTree(pHead1->left, pHead2);
		}

		if (!ret) {
			ret = hasSubTree(pHead1->right, pHead2);
		}
	}

	return ret;
} 