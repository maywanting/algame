class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for i in range(n+1)] for j in range(m+1)]
        matrix[0][1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    matrix[i+1][j+1] = 0
                else:
                    matrix[i+1][j+1] = matrix[i][j+1] + matrix[i+1][j]

        return matrix[m][n]
solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
