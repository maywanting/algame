class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        i = j = 0
        matrix[0][0] = 1
        value = 2
        while True:
            while (j < n-1) and matrix[i][j+1] == 0:#right
                j += 1
                matrix[i][j] = value
                value += 1
            while (i < n-1) and matrix[i+1][j] == 0:#down
                i += 1
                matrix[i][j] = value
                value += 1
            while (j > 0) and matrix[i][j-1] == 0: #left
                j -= 1
                matrix[i][j] = value
                value += 1
            while (i > 0) and matrix[i-1][j] == 0: #up
                i -= 1
                matrix[i][j] = value
                value += 1
            if value > n*n:
                break
        return matrix

solution = Solution()
print(solution.generateMatrix(5))
