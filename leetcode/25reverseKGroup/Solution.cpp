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
    printList(solution.reverseKGroup(&head1, 3));
    return 0;
}
