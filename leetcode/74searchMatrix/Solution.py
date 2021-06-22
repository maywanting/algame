class Solution(object):
    def searchMatrix(self, matrix, target):
        colNum = len(matrix)
        rowNum = len(matrix[0])

        si = 0
        ei = colNum*rowNum -1

        while si <= ei:
            mid = (si + ei) / 2
            midValue = matrix[mid/rowNum][mid%rowNum]

            if midValue == target:
                return True
            elif target < midValue:
                ei = mid - 1
            else:
                si = mid + 1

        return False


    #first
    def searchMatrix1(self, matrix, target):
        if target < matrix[0][0] or target > matrix[-1][-1]:
            # return -1
            return False

        for i in range(len(matrix)-1):
            if matrix[i+1][0] == target:
                # return 1
                return True
            elif matrix[i+1][0] > target:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        # return 2
                        return True
                    elif matrix[i][j] > target:
                        # return -3
                        return False

                # return -2
                return False

        for j in range(len(matrix[0])):
            if matrix[-1][j] == target:
                # return 3
                return True
            elif matrix[-1][j] > target:
                # return -4
                return False


solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 16))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 21))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(solution.searchMatrix([[1]], 1))
