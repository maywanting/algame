class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        if (n == 0):
            return []
        m = len(matrix[0])
        res = []
        k = 0
        while (n > 1) and (m > 1):
            res += matrix[k][k:m+k] #right
            print(res)

            #down
            for i in range(k+1, n-1+k):
                res += [matrix[i][m-1+k]]

            print(res)
            #left
            res += matrix[n-1+k][::-1][k:m+k]

            print(res)
            #up
            for j in range(n-2+k, k, -1):
                res += [matrix[j][k]]
            print(res)
            n -= 2
            m -= 2
            k += 1

        if n == 1: #right
            res += matrix[k][k:m+k]
        elif m == 1: #down
            for i in range(k, n+k):
                res += [matrix[i][m-1+k]]
        return res

solution = Solution()
# print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.spiralOrder([[1,2,3],[5,6,7],[9,10,11],[13,14,15],[17,18,19]]))

