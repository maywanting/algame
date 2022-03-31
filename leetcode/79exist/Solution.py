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

solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(solution.exist([["a"]], "a"))
print(solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
