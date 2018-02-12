Merge k Sorted Lists
---

# Description

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Solution

The first soultion I have thoughted is find the smallest number of all the lists and combined it with the target list. I think the time complexity is O(Klog(K)log(N)), N is the average node length of all the lists, k is the number of lists. Space complexity is O(1), we don't need more space.

However, this solution is not accepted by the system because of the last test case is time out. And the last test case is the worest condition of this algothrim. N is 1 and K is very big, so the K determine the time that this prograpm running.

Another problem of this solution is the head of result list. The head should have number and the number is lower than any number in the lists.

``` C++
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode head = ListNode(-100000);
        ListNode *p = &head;

        mergeRestLists(p, lists, 0, -100001);
        return head.next;
    }

    ListNode* mergeRestLists(ListNode* head, vector<ListNode*>& lists, int index, int standard) {
        if (index >= lists.size()) {
            return head;
        }

        while (lists[index] != NULL) {
            if (standard < head->val || standard > lists[index]->val) {
                head = mergeRestLists(head, lists, index + 1, lists[index]->val);

                head->next = lists[index];
                head = head->next;
                lists[index] = lists[index]->next;
                head->next = NULL;
            } else {
                head = mergeRestLists(head, lists, index + 1, standard);
                return head;
            }
        }

        head = mergeRestLists(head, lists, index + 1, standard); //排除之后还有
        return head;
    }
};
```

So, to pass the last case, I have to find another way. The another solution of this problem is merge every two lists until lists number is one. First time I have thought about this, and the time complexity is O(Nlog(K)). It looks like very good solution, but if the N is large, we need to scanned each numbers at least k/2 times.

However, this solution is a good way to solve the last test case, So, I also write this problem.

``` C++
class Solution {
public:
    ListNode *mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (NULL == l1) return l2;
        else if (NULL == l2) return l1;
        if (l1->val <= l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty()) return NULL;
        int len = lists.size();
        while (len > 1) {
            for (int i = 0; i < len / 2; ++i) {
                lists[i] = mergeTwoLists(lists[i], lists[len - 1 - i]);
            }
            len = (len + 1) / 2;
        }

        return lists.front();
    }
};
```
