Set Matrix Zeroes
---

# Description
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Solution

Since in-place operation is required, we should scan the matrix twice. First is to memorry which column and which row need to be zero. Second is to modify the matrix.

``` python
class Solution(object):
    def setZeros(self, matrix):
        mLen = len(matrix)
        nLen = len(matrix[0])
        m = [1] * mLen
        n = [1] * nLen
        for i in range(mLen):
            for j in range(nLen):
                if matrix[i][j] == 0:
                    m[i] = 0
                    n[j] = 0

        for i in range(mLen):
            if m[i] == 0:
                matrix[i] = [0] * nLen
            else:
                for j in range(nLen):
                    if n[j] == 0:
                        matrix[i][j] = 0

        return matrix
```
