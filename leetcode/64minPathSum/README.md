Minimun Path Sum
---

# Description

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# Solution

This is also an extension of Q62. The difference is the path add the weights. So when we need to find the smaller weight of two pathes.

``` python
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][0] = grid[0][0]
        for i in range (n-1):
            matrix[0][i+1] = matrix[0][i] + grid[0][i+1]

        for i in range(m-1):
            matrix[i+1][0] = matrix[i][0] + grid[i+1][0]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]

        return matrix[-1][-1]
```
