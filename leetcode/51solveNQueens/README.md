N-Queens
---

# Description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Examples

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

# Solution

N-Queens is a famous problem, the rule is as below: all the queens can not be in one line, in one column, in one diagonal.

not in one line: create 1 dimensional array to store the position of queens
not in one column: make sure that all the value in array is different
not in one diagonal: there are twoo diagonal line.
- the left to right line: the difference of index and value is same.
- the right to left line: the sum of index and value is same.

``` python
class Solution(object):
    def solveNQueens(self, n):
        self.res = []
        self.number = n;
        self.dfs([], [], [])
        return self.res

    def dfs(self, queens, ij_diff, ij_sum): #ij_diff right; ij_sum left
        if len(queens) == self.number:
            matrix = ['' for k in range(self.number)]
            for k in range(self.number):
                for i in range(self.number):
                    if i == queens[k]:
                        matrix[k] += 'Q'
                    else:
                        matrix[k] += '.'
            self.res += [matrix]
        j = len(queens)
        for i in range(self.number):
            if (i not in queens) and (i+j not in ij_sum) and (j-i not in ij_diff) :
                self.dfs(queens + [i], ij_diff + [j-i], ij_sum + [j+i])
```
