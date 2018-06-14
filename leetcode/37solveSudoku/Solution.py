class Solution(object):
    def solveSudoku(self, board):
        # find the .
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    field = this.getValidNumber(board, i, j)

    def getValidNumber(self, board, x, y):
        number = []
        for i in range(1, 9):
            # row
            if i in board[x]:
                continue
            if i in board[:][y]:
                continue
            if i in board[x/3]

solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
print(board)
