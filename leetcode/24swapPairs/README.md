Swap Nodes in Pairs
---

# Description

Given a linked list, swap every two adjacent nodes and return its head.

For example, Given `1->2->3->4`, you should return the list as `2->1->4->3`.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Solution

This Problem is very easy. The most important thing is dealing with the swaption of two nodes in lists.

``` C++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode node = ListNode(0);
        node.next = head;

        ListNode* front, *p1, *p2;
        front = &node;
        while (true) {
            p1 = front->next;
            if (p1 == NULL){
                break;
            }

            p2 = p1->next;
            if (p2 == NULL) {
                break;
            }

            p1->next = p2->next;
            p2->next = p1;
            front->next = p2;
            front = p1;
        }

        return node.next;
    }
};
```
