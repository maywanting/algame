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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == NULL) {
            return NULL;
        }

        ListNode* front = head;
        ListNode* temp = new ListNode(0);
        temp->next = head;
        head = temp;
        ListNode* end = head;

        //make the front in the right position
        for (int i = 1; i < n; i++) {
            front = front->next;
        }

        while (front->next) {
            front = front->next;
            end = end->next;
        }
        temp = end->next;
        end->next = temp->next;
        return head->next;
    }
};

int main() {
    // int arr1[1] = {1};
    int arr1[3] = {1, 2, 3};
    // int arr1[5] = {1, 2, 3, 4, 5};
    ListNode l1 = ListNode(arr1[0]);
    ListNode *p1 = &l1;

    for (int i = 1; i < 3; i++) {
        ListNode * tempNode = new ListNode(arr1[i]);
        p1->next = tempNode;
        p1 = p1->next;
    }

    Solution solution;
    printList(solution.removeNthFromEnd(&l1, 3));
    return 0;
}
