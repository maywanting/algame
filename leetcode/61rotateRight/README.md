Rotate List
---

# Description

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

# Solution

When we connect the end node to the first node, then we can gain a circle. So the question is to calculate which node can be head.

One of input parameters is k. k means we need to anticlockwise rotate the head to gain the head node. However, we also can clockwise rotate the head with `length-k` steps to gain the final head node.

``` cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) {
            return NULL;
        }
        int length = 1;
        ListNode* p, *q;
        p = q = head;
        while (q->next) {
            length ++;
            q = q->next;
        }
        k = length - (k % length);
        cout << length << endl;

        q->next = p;

        for (int i = 0; i < k; i++) {
            p = p->next;
            q = q->next;
        }
        q->next = NULL;
        return p;
    }
};
```
