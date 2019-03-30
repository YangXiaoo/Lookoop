// 2019-3-30
#include <stdio.h>
#include <vector>
using namespace std;

void MirrorRecursively(TreeNode* pHead) {
	if (pHead == nullptr) return;

	if (pHead->left == nullptr && pHead->right == nullptr) return;

	TreeNode* tmp = pHead->left;
	pHead->left = pHead->right;
	pHead->right = tmp;

	if (pHead->left) 
		MirrorRecursively(pHead->left);
	if (pHead->right)
		MirrorRecursively(pHead->right);
}