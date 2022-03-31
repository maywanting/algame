Word Search
---

# Description

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?

# Solution

There are four directions to seach the next character in each step. So, we need to use DFS to solve this question.

We should mark the matched character when we search. Another words, According to the time limitations, we need to mark in the original board. After seaching the board, we need to recover the marked character.

``` python
class Solution(object):
    def search(self, board, word, i, j):
        m = len(board)
        n = len(board[0])

        if (board[i][j] == word[0]):
            board[i][j] = 1 # mark
            if len(word) == 1:
                return True
            if (i+1 < m) and self.search(board, word[1:], i+1, j): #down
                return True
            if (j+1 < n) and self.search(board, word[1:], i, j+1): #right
                return True
            if (i-1 >= 0) and self.search(board, word[1:], i-1, j): #up
                return True
            if (j-1 >= 0) and self.search(board, word[1:], i, j-1): #left
                return True
            board[i][j] = word[0] # recover
        return False

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j):
                    return True
        return False
```