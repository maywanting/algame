Reverse Nodes in k-Group
---

# Description

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example, Given this linked list: `1->2->3->4->5`

For k = 2, you should return: `2->1->4->3->5`

For k = 3, you should return: `3->2->1->4->5`

# Solution

This problem is the extented version of last problem. So, how to deal with it. The solution can be described as this.

Set three pointer in this list. Given list does not have the head node, so creating head node.

```
head->1->2->3->4->5
  |   |  |
front p  q

head->2->1->3->4->5
  |      |  |
front    p  q

head->3->2->2->4->5
  |         |  |
front       p  q
```

This is reversing process when k is 4. So move the next node of p to the head's next node. p is the first node of every k-number nodes. when p's next node all have been moved, than start another k-number nodes reversing.

``` C++
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode node = ListNode(0);
        node.next = head;

        ListNode* front, *p, *q, *end;
        front = &node;
        while (true) {
            //confirm the rest number is enough
            int number = k;
            end = front->next;
            while (number--) {
                if (end == NULL) {
                    return node.next;
                }
                end = end->next;
            }

            number = k - 1;
            p = front->next;
            q = p->next;
            while (number--) {
                //move q to the end of front
                p->next = q->next;
                q->next = front->next;
                front->next = q;

                q = p->next;
            }
            front = p;
        }
    }
};
```
