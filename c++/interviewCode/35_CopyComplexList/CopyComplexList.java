// 2019-4-18
// 复制复杂链表
// letcode 138
import java.uitl.*;

// 定义节点
class ListNode {
	int val;
	ListNode next, random;
	public ListNode(int val) {
		this.val = val;
	}
}

public class CopyComplexList {
	public ListNode copyList(ListNode head) {
		// 复制节点
		copyNode(head);
		// 连接随机节点
		linkRandom(head);
		// 删除新旧链表连接
		LinkNode newHead = removeNode(head);
		return newHead;
	}

	public void copyNode(ListNode head) {
		if (head == null)
			return;

		ListNode pHead = head;
		while (pHead != null) {
			ListNode newNode = new ListNode(pHead.val);
			newNode.next = pHead.next;
			pHead.next = newNode;
			newNode.random = pHead.random;
			pHead = next;
		}
	}

	public void linkRandom(ListNode head) {
		if (head == null) 
			return;

		ListNode pHead = head;
		while (pHead != null) {
			ListNode nextNode = pHead.next;				// 获得新链表节点
			// nextNodeRandom = nextNode.random;	// 新链表random连在在旧链表的节点
			// randomNode = nextNodeRandom.next;	// 获得旧random的下一个点
			// nextNode.random = randomNode;		// 新random
			if (newNode.random != null) {
				newNode.random = newNode.random.next;
			}
			pHead = nextNode.next;
		}
	}

	public ListNode removeNode(ListNode head) {
		if (head == null) return head;

		ListNode pHead = head;
		ListNode newHead = head;
		ListNode dummyHead = newHead;

		while (pHead != null) {
			newHead = pHead.next;			// 新链表节点
			pHead.next = nextNode.next;		// 连接旧链表
			pHead = nextNode.nextNode;		// 获得下一个循环的头结点
			if (pHead != null) {			// 连接新链表
				newHead.next = pHead.next;
			}
		}

		return dummyHead.next;
	}
}