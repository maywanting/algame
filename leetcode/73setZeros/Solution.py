class Solution(object):
    def setZeros(self, matrix):
        mLen = len(matrix)
        nLen = len(matrix[0])
        m = [1] * mLen
        n = [1] * nLen
        for i in range(mLen):
            for j in range(nLen):
                if matrix[i][j] == 0:
                    m[i] = 0
                    n[j] = 0

        for i in range(mLen):
            if m[i] == 0:
                matrix[i] = [0] * nLen
            else:
                for j in range(nLen):
                    if n[j] == 0:
                        matrix[i][j] = 0

        return matrix

solution = Solution()
# print(solution.setZeros([[1,1,1],[1,0,1],[1,1,1]]))
# print(solution.setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(solution.setZeros([[0,1,0,2],[3,4,5,2],[1,3,1,5]]))
print(solution.setZeros([[0,1,3,2],[3,4,0,2],[1,3,1,5]]))
