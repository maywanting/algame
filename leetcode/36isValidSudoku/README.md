Valid Sudoku
---

# Description

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

## Note:

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# Solution

The most import point is the words in note. This problem is just to find the repeated number in every row and every column and every 3*3 vector without '.'. So, we can use `set` to remove the repeated number and make judgement according to the length of set.

``` python
class Solution(object):
    def isValidSudoku(self, board):
        rowV, colV, subV = [], [], []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    rowV += [(i, value)]
                    colV += [(j, value)]
                    subV += [(i/3, j/3, value)]

        return (len(rowV) == len(set(rowV))) and (len(colV) == len(set(colV))) and (len(subV) == len(set(subV)))
```
