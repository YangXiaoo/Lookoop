/*
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
*/
// 2019-11-28
function ListNode(x){
    this.val = x;
    this.next = null;
}

function printListFromTailToHead(head)
{
    var arr = [];
    while (head !== null) {
        arr.unshift(head.val);
        head = head.next;
    }

    return arr;
}


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


function test() {
    var arr = [1,2,3,4,5,6];
    var linkedList = getLinkedListFromArray(arr);
    var ret = printListFromTailToHead(linkedList);
    console.log(ret.join());
}

test();