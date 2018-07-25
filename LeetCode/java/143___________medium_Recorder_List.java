/**
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/

// 2018-7-25
// 143. Recorder List
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// ??????
class 143_medium_Recorder_List {
    public void reorderList(ListNode head) {
        if (head == null) return;
        Deque<ListNode> queue = new LinkedList<>();
        ListNode dummy = head;
        while (dummy != null) {
            queue.offer(dummy);
            dummy = dummy.next;
        }
        head = queue.pollFirst();
        while (!queue.isEmpty() && head != null) {
            ListNode tmp;
            tmp = queue.poll();
            head.next = tmp;
            tmp = queue.pollLast();
            if (tmp == null) break;
            head.next.next = tmp;
            head = head.next.next.next;
        }

        return;
    }
}