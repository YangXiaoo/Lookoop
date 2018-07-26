/**
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
 */

// 2018-7-26
// 147. Insertion Sort List
// https://leetcode-cn.com/problems/insertion-sort-list/description/
// https://www.cnblogs.com/puyangsky/p/6480942.html
// https://www.cnblogs.com/ProWhalen/p/5382739.html
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class 147_medium_Insertion_Sort_List {
    public ListNode insertionSortList(ListNode head) {
    if(head==null || head.next == null)
        return head;

    ListNode pre = new ListNode(-1);
    ListNode ans = pre;
    ListNode cur = head;

    while (cur != null) {
        pre = ans;
        while (pre.next != null && pre.next.val < cur.val) {
            pre = pre.next;
        }
        ListNode tmp = cur.next;
        cur.next = pre.next;
        pre.next = cur;
        cur = tmp;
    }
    return ans.next;
}