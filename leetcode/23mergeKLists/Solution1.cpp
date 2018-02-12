#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void printList(ListNode* l) {
    while(l != NULL) {
        cout << l->val << " ";
        l = l->next;
    }
    cout << "\n";
}

void printVector(vector<ListNode*>& lists) {
    for (int i = 0; i < lists.size(); i++) {
        printList(lists[i]);
    }
}

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

void createList(int* arr, int length, ListNode* head) {
    *head = ListNode(arr[0]);
    ListNode *p1 = head;

    for (int i = 1; i < length; i++) {
        ListNode * tempNode = new ListNode(arr[i]);
        p1->next = tempNode;
        p1 = p1->next;
    }
}

int main() {
    // int arr1[4] = {1, 3, 5, 8};
    // int arr2[3] = {0, 6, 7};
    // int arr3[6] = {3, 4, 6, 9, 12, 14};
    int arr1[0] = {};
    int arr2[1] = {-2};
    int arr3[3] = {-3, -2, 1};

    vector<ListNode*> vec;
    // ListNode head1 = ListNode(0);
    ListNode *head1 = NULL;
    // createList(arr1, 0, &head1);
    vec.push_back(head1);

    ListNode head2 = ListNode(0);
    createList(arr2, 1, &head2);
    vec.push_back(&head2);

    ListNode head3 = ListNode(0);
    createList(arr3, 3, &head3);
    vec.push_back(&head3);

    printVector(vec);

    Solution solution;
    printList(solution.mergeKLists(vec));
    return 0;
}
