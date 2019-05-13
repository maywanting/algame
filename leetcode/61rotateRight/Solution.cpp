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
    int arr1[5] = {1, 2, 3, 4, 5};
    ListNode head1 = ListNode(0);
    createList(arr1, 5, &head1);

    Solution solution;
    printList(&head1);
    printList(solution.rotateRight(&head1, 2));
    return 0;
}
