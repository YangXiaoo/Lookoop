/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* ans = new ListNode(0);
        ListNode* pre = ans;
        while (head != nullptr) {
            pre = ans;
            while (pre && pre->next && pre->next->val < head->val) {
                pre = pre->next;
            }
            
            ListNode* tmp = head->next;
            head->next = pre->next;
            pre->next = head;
            head = tmp;
        }
        
        return ans->next;
    }
};