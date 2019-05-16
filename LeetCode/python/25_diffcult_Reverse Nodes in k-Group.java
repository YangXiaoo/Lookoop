/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int count = 0;
        ListNode cur = head;
        ListNode pre = head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode dummyHead = dummy;
        while (cur != null) {
            ++count;
            ListNode nextNode = cur.next;
            if (count == k) {
                ListNode curHead = reverseRange(pre, cur);
                dummy.next = curHead;
                pre.next = nextNode;
                dummy = pre;
                pre = nextNode;
                count = 0;
            }
            cur = nextNode;
        }
        
        return dummyHead.next;
    }
    
    public ListNode reverseRange(ListNode start, ListNode end) {
        ListNode pre = null;
        while (start != end) {
            ListNode nextNode = start.next;
            start.next = pre;
            pre = start;
            start = nextNode;
            
        }
        end.next = pre;
        return end;
    }
}