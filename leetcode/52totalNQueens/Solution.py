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

solution = Solution()
print(solution.totalNQueens(4))
