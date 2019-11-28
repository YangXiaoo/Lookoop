// util.js

// 链表节点
function ListNode(x){
    this.val = x;
    this.next = null;
}

// 通过数组生成链表
function getLinkedListFromArray(arr) {
    var head = new ListNode(0);
    var dummy = head;
    for (let v of arr) {
        var curNode = new ListNode(v);
        head.next = curNode;
        head = curNode;
    }

    return dummy.next;
};

// 中序遍历树
function InorderTraversal(root) {
    if (root !== null) {
        InorderTraversal(root.left);
        console.log(root.val);
        InorderTraversal(root.right);
    }
}

export {getLinkedListFromArray, InorderTraversal};