/**
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

*/

// 2018-7-24
// 138. Copy List with Random Pointer
// https://blog.csdn.net/edwal/article/details/46912979
// https://blog.csdn.net/derrantcm/article/details/47745459
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class 138_medium_Copy_List_with_Random_Pointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return head;

        // 1. 插入节点
        insertNode(head);
        // 2. 将random指向对应元素的next元素
        linkRandom(head);
        // 3. 分离新链表与旧链表
        return splitList(head);
    }

    private void insertNode(RandomListNode head) {
    	RandomListNode node = head;
    	while (node != null) {
    		RandomListNode newNode = new RandomListNode(node.label);
    		newNode.next = node.next;
    		newNode.random = node.random;
    		node.next = newNode;
    		node = newNode.next;
    	}
    }

    private void linkRandom(RandomListNode head) {
    	RandomListNode node = head;
    	while (node != null) {
    		RandomListNode newNode = node.next;
    		if (newNode.random != null) {
    			newNode.random = newNode.random.next;
    		}
    		node = newNode.next;
    	}
    }

    private RandomListNode splitList(RandomListNode head) {
    	RandomListNode dummy = head.next;
    	RandomListNode node = head;
    	RandomListNode cur;

    	while (node != null) {
    		cur = node.next;
    		node.next = cur.next; // 旧链表连接
    		node = cur.next;
    		if (node != null) {
    			cur.next = node.next;
    		}
    	}

    	return dummy;
    }
}