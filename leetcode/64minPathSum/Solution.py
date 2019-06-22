class Solution(object):

    def dfs(self, left, down, temSum):
        print("============")
        print(left)
        print(down)
        print(temSum)
        if left < self.m:
            self.dfs(left + 1, down, temSum + self.grid[down][left+1])
        if down < self.n:
            self.dfs(left, down + 1, temSum + self.grid[down+1][left])
        # print(">>>>" + str(temSum))
        if (left + down) >= (self.m + self.n):
            print(">>>>" + str(temSum))
            if temSum < self.res:
                self.res = temSum

    def minPathSum1(self, grid):
        self.m = len(grid[0]) -1
        self.n = len(grid) -1
        self.res = sum(grid[0])
        self.grid = grid
        for g in grid:
            self.res += g[-1]
        self.dfs(0, 0, grid[0][0])
        return self.res

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][0] = grid[0][0]
        for i in range (n-1):
            matrix[0][i+1] = matrix[0][i] + grid[0][i+1]

        for i in range(m-1):
            matrix[i+1][0] = matrix[i][0] + grid[i+1][0]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]

        return matrix[-1][-1]

solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
# print(solution.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))
