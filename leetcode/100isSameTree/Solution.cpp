#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if (p == NULL) {
            return q == NULL;
        } else {
            return (q == NULL) ? false : (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};

int main() {
    return 0;
}
#include <iostream>

using namespace std;

class Solution {
public:
    isSameTree() {
    }
};

int main() {
    return 0;
}
