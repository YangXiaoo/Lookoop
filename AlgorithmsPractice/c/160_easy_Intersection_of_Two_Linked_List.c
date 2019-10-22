/**
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
*/

// 2018-7-30
// 160. Intersection of Two Linked Lists
// https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/

#include <stdio.h>

int findMin(int *nums, int numsSize);

int main()
{
  // Can not do anthing! 
}
 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int lens(struct ListNode *head)
{
    int length = 0;
    struct ListNode *p = head;
    while (p != NULL)
    {
        length++;
        p = p->next;
    }

    return length;
}
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int A_lens = lens(headA);
    int B_lens = lens(headB);
    int gap = A_lens - B_lens > 0 ? A_lens - B_lens : B_lens - A_lens;

    struct ListNode *plong = headA;
    struct ListNode *pshort = headB;

    if (A_lens < B_lens) 
    {
        plong = headB;
        pshort = headA;
    }

    for (int i = 0; i < gap; i++)
    {
        plong = plong->next;
    }

    while (plong && pshort && plong->val != pshort->val)
    {
        plong = plong->next;
        pshort = pshort->next;
    }

    return pshort;
}