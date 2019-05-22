Unique Paths
---

# Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

# Solution

This is a kind of DP. And the solution of this problem is like solve Fibonacci number.

We set a matrix to store all the situation. We set the grid as below.

G[i-1][j-1] G[i-1][j]
G[i][j-1]   G[i][j]

So to reach Grid[i][j], there are two ways: through G[i-1][j] and through G[i][j-1]. So the paths to reach G[i][j] is equal G[i-1][j] plus G[i][j-1].

``` python
class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[0 for i in range(m+1)] for j in range(n+1)]
        matrix[1][0] = 1

        for j in range(1, n+1):
            for i in range(1, m+1):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]

        return matrix[n][m]
```
