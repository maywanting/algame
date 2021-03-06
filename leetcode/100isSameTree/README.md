Same Tree
---

# Description

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

# Solution

Just traversing the tree and compare. One thing should be noticed is the end node.

``` cpp
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
```


---

# Description

# Solution

