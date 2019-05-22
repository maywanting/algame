class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[0 for i in range(m+1)] for j in range(n+1)]
        matrix[1][0] = 1

        for j in range(1, n+1):
            for i in range(1, m+1):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]

        print(matrix)
        return matrix[n][m]

solution = Solution()
print(solution.uniquePaths(7, 3))
