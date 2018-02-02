Remove Nth Node From End of List
---

# Description

Given a linked list, remove the nth node from the end of list and return its head.

For example, Given linked list: `1->2->3->4->5`, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Try to do this in one pass.

# Solution

This is a problem about linked list. So I choose C++ to deal with it. I think the most difficult thing is how to delete the first node. So, when i solve this problem, segmentation fault always occured.

``` C++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == NULL) {
            return NULL;
        }

        ListNode* front = head;
        ListNode* temp = new ListNode(0);
        temp->next = head;
        head = temp;
        ListNode* end = head;

        //make the front in the right position
        for (int i = 1; i < n; i++) {
            front = front->next;
        }

        while (front->next) {
            front = front->next;
            end = end->next;
        }
        temp = end->next;
        end->next = temp->next;
        return head->next;
    }
};
```
