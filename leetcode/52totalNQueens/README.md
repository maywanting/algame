N-Queens II
---

# Description

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

# Solution

This problem is similar with the last problem. Just return the number of last question's results.


``` python
class Solution(object):
    def totalNQueens(self, n):
        self.resNum = 0
        self.number = n
        self.dfs([], [], [])
        return self.resNum

    def dfs(self, queens, ij_diff, ij_sum): #ij_diff right; ij_sum left
        if len(queens) == self.number:
            self.resNum += 1
        j = len(queens)
        for i in range(self.number):
            if (i not in queens) and (i+j not in ij_sum) and (j-i not in ij_diff) :
                self.dfs(queens + [i], ij_diff + [j-i], ij_sum + [j+i])
```
