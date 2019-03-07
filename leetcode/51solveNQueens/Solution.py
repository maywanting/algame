class Solution(object):
    def solveNQueens(self, n):
        self.res = []
        self.number = n;
        # queens = [0 for i in range(n)]
        self.dfs([], [], [])
        # for d1 in self.res:
            # for d2 in d1:
                # print(d2)
            # print("---------")
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

solution = Solution()
print(solution.solveNQueens(4))
