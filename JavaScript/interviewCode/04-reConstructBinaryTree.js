/*
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
*/
// 2019-11-28
 function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} 

function reConstructBinaryTree(pre, vin)
{
	var pLeft = 0, pRight = pre.length-1, vLeft = 0, vRight = vin.length-1;
    var root = helper(pre, pLeft, pRight, vin, vLeft, vRight);

    return root;
}

function helper(pre, pLeft, pRight, vin, vLeft, vRight) {
	if (pLeft > pRight || vLeft > vRight) {
		return null;
	}

	var curRoot = new TreeNode(pre[pLeft]);	// 当前根节点

	// 在中序遍历序列中找到当前的根节点索引
	var curRootIndexInVin = vLeft;
	for (var i = vLeft; i <= vRight; ++i) {
		if (pre[pLeft] === vin[i]) {
			curRootIndexInVin = i;
			break;
		}
	}

	var len = curRootIndexInVin - vLeft;
	curRoot.left = helper(pre, pLeft+1, pLeft+len+1, vin, vLeft, curRootIndexInVin-1);
	curRoot.right = helper(pre, pLeft+len+1, pRight, vin, curRootIndexInVin+1, vRight);

	return curRoot;
}

function InorderTraversal(root) {
    if (root !== null) {
        InorderTraversal(root.left);
        console.log(root.val);
        InorderTraversal(root.right);
    }
}

function test() {
	var pre = [1,2,4,7,3,5,6,8], vin = [4,7,2,1,5,3,8,6];
	var retRoot = reConstructBinaryTree(pre, vin);
	InorderTraversal(retRoot);
}

test();