#include <iostream>

/**
 * describe:
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */

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
    acds
};

int main() {
    // int arr1[5] = {2, 4, 3, 9, 8};
    // int arr2[5] = {5, 6, 4, 8, 3};
    // int arr1[1] = {5};
    // int arr2[1] = {5};
    int arr1[9] = {0,8,6,5,6,8,3,5,7};
    int arr2[9] = {6,7,8,0,8,5,8,9,7};
    ListNode l1 = ListNode(arr1[0]);
    ListNode l2 = ListNode(arr2[0]);

    ListNode *p1 = &l1;
    ListNode *p2 = &l2;

    for (int i = 1; i < 9; i++) {
        ListNode * tempNode = new ListNode(arr1[i]);
        p1->next = tempNode;
        p1 = p1->next;
    }

    for (int i = 1; i < 9; i++) {
        ListNode * tempNode = new ListNode(arr2[i]);
        p2->next = tempNode;
        p2 = p2->next;
    }

    Solution testClass;
    printList(&l1);
    printList(&l2);
    printList(testClass.addTwoNumbers(&l1, &l2));
    return 0;
}
