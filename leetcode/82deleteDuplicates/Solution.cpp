#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p, *q;
        ListNode *s = new ListNode(-101);
        s->next = head;
        head = s;
        q = s->next;
        bool flag = false;

        while(q) {
            p = s->next;
            q = p->next;
            while (q && (p->val == q->val)) {
                q = q->next;
                flag = true;
            }

            if (flag){ 
                s->next = q;
                flag = false;
            } else {
                s = s->next;
            }
        }

        return head->next;
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
    // int arr1[7] = {1, 2, 3, 3, 4, 4, 5};
    // ListNode head1;
    // createList(arr1, 7, &head1);

    // Solution solution;
    // printList(&head1);
    // printList(solution.deleteDuplicates(&head1));

    int arr2[6] = {1, 1, 1, 2, 3, 3};
    ListNode *head2;
    createList(arr2, 6, head2);

    Solution solution;
    printList(head2);
    printList(solution.deleteDuplicates(head2));

    // int arr3[3] = {1, 1, 3};
    // ListNode * head3;
    // createList(arr3, 3, head3);

    // Solution solution;
    // printList(head3);
    // printList(solution.deleteDuplicates(head3));

    return 0;
}
