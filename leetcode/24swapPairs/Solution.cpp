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
    // int arr1[4] = {1, 2, 3, 4};
    int arr1[5] = {1, 2, 3, 4, 5};
    ListNode head1 = ListNode(0);
    createList(arr1, 5, &head1);

    Solution solution;
    printList(solution.swapPairs(&head1));
    return 0;
}
