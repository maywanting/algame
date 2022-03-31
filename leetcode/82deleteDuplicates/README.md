Remove Duplicates from Sorted List II
---

# Description

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

# Solution

I'm used to using C++ to deal with this list problem. But, In this problem,`bus error` often occurs. 

This problem is not so difficult. The only troublesome point is to delete the duplicate number, not make the number to be one.

``` cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p, *q;
        ListNode *s = new ListNode(-101);
        s->next = head;
        head = s;
        q = s->next;
        bool flag = false;

        while(q) {
            p = s->next;
            q = p->next;
            while (q && (p->val == q->val)) {
                q = q->next;
                flag = true;
            }

            if (flag){ 
                s->next = q;
                flag = false;
            } else {
                s = s->next;
            }
        }

        return head->next;
    }
};
```