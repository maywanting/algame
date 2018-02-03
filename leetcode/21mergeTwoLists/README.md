Merge Two Sorted Lists
---

# Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## Example

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

# Solution

This problem is too easy that to be lazy to describe the solution. The only one thing should be noiced that the return is also sorted linked list.

``` C++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(0);
        ListNode *end = res;
        int value;
        while (l1 || l2) {
            if (l1 == NULL) {
                value = l2->val;
                l2 = l2->next;
            } else if (l2 == NULL) {
                value = l1->val;
                l1 = l1->next;
            } else if (l1->val < l2->val) {
                value = l1->val;
                l1 = l1->next;
            } else {
                value = l2->val;
                l2 = l2->next;
            }
            ListNode *temp = new ListNode(value);
            end->next = temp;
            end = end->next;
        }
        return res->next;
    }
};
```
