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

solution = Solution()
vec = [
    [".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]
]
print(solution.isValidSudoku(vec))
