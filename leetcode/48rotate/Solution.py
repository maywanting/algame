class Solution(object):
    def rotate(self, matrix):
        last = len(matrix) - 1
        for i in range((last + 1) / 2):
            for j in range((last + 2) / 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[last - j][i] # 4 -> 1
                matrix[last - j][i] = matrix[last - i][last - j] #3->4
                matrix[last - i][last - j] = matrix[j][last - i] #2->3
                matrix[j][last - i] = temp #1->2
        return matrix

solution = Solution()
print(solution.rotate([[1]]))
print(solution.rotate([[1, 2], [3, 4]]))
# print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
# print(solution.rotate([ [ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16] ]))
