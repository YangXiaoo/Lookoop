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
        ListNode _cur = head;
        int lens = 0;
        while (_cur !=null) {
            _cur = _cur.next;
            ++lens;
        }
        
        if (lens == 0) {
            return head;
        }
        
        if (lens < k) {
            return head;
        }

        int count = 0;
        ListNode cur = head;
        ListNode pre = head;
        ListNode dummy = new ListNode(0);
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