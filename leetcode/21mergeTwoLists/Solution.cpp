#include <iostream>

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

int main() {
    int arr1[3] = {1, 2, 4};
    int arr2[3] = {1, 3, 4};
    ListNode l1 = ListNode(arr1[0]);
    ListNode l2 = ListNode(arr2[0]);
    ListNode *p1 = &l1;
    ListNode *p2 = &l2;

    for (int i = 1; i < 3; i++) {
        ListNode * tempNode1 = new ListNode(arr1[i]);
        ListNode * tempNode2 = new ListNode(arr2[i]);
        p1->next = tempNode1;
        p1 = p1->next;
        p2->next = tempNode2;
        p2 = p2->next;
    }

    Solution solution;
    printList(solution.mergeTwoLists(&l1, &l2));
    return 0;
}
