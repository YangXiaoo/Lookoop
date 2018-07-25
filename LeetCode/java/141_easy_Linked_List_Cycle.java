/**
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
*/

// 2018-7-24
// 141. Linked List Cycle
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
// TLE
public class 141_easy_Linked_List_Cycle {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();

        while (head != null) {
            if (set.contains(head)) {
                return true;
            } else {
                set.add(head);
            }
            head = head.next;
        }

        return false;
    }
}

// 使用双指针法，若有环则慢的会追赶上快的指针

public class Solution {
   public boolean hasCycle(ListNode head) {
        if (head == null) return null;
        ListNode fast = head;
        ListNode slow = head;

        while  (fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == null) return null;

            if (fast == slow) return true;
        }

        return false;
    }
}