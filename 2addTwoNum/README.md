Add Two Numbers
---

# Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Examples

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

# Solution

This question is very easy. Maybe the descrption of this question is not easy to understand. In fact, this is just a question to get the sum of two numbers, and each linded node is allowed in one character.

This question i used C++.

I think it's a chance for me to remember the linked list in C++

``` C++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum, next = 0;
        ListNode res = ListNode(0);
        ListNode *p = &res;
        ListNode *tempNode = new ListNode(0);

        while (l1 != NULL || l2 != NULL) {
            sum = next;
            if (l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;
            }
            if ((sum / 10) > 0) {
                next = sum / 10;
            } else {
                next = 0;
            }
            tempNode = new ListNode(sum % 10);
            p->next = tempNode;
            p = p->next;
        }
        if (next > 0) {
            tempNode = new ListNode(next);
            p->next = tempNode;
        }

        return res.next;
    }
};
```

By the way, to run c++ program, `g++` will be used to compile the program. And then the `a.out` file will be created. So excueting the `a.out` file and then will get the result.

