/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode dummyHead = dummy;
        ListNode cur = head;

        while (cur != null) {
            ListNode nextNode = cur.next;
            // System.out.println(cur.val);
            if (nextNode != null) {
                ListNode nextCur = nextNode.next;
                nextNode.next = cur;
                dummyHead.next = nextNode;
                cur.next = nextCur;
                dummyHead = cur;
                cur = nextCur;
            } else {
                dummyHead.next = cur;
                dummyHead = cur;
                cur = nextNode;
            }
        }
        
        return dummy.next;
    }
}