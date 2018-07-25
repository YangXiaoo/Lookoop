/**
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
*/

// 2018-7-25
// 142. Linked List Cycle II
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class 142_hard_Linked_List_Cycle_II {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();

        while (head != null) {
            if (set.contains(head)) {
                return head;
            } else {
                set.add(head);
            }
            head = head.next;
        }

        return null;
    }
}

// https://blog.csdn.net/willduan1/article/details/50938210
public class Solution {
    public ListNode detectCycle( ListNode head ) {
		if( head == null || head.next == null ){
			return null;
		}
		// 快指针fp和慢指针sp，
        ListNode fp = head, sp = head;
        while( fp != null && fp.next != null){
        	sp = sp.next;
        	fp = fp.next.next;
        	//此处应该用fp == sp ，而不能用fp.equals(sp) 因为链表为1 2 的时候容易
        	//抛出异常
        	if( fp == sp ){  //说明有环
        		break;
        	}
        }
        //System.out.println( fp.val + "   "+ sp.val );
        if( fp == null || fp.next == null ){
        	return null;
        }
        //说明有环，求环的起始节点
        sp = head;
        while( fp != sp ){
        	sp = sp.next;
        	fp = fp.next;
        }
        return sp;
    }
}
