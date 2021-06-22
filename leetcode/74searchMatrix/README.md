Search a 2D Matrix
---

# Description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

# Solution

Use Binary search, and regard the 2D matrix as sorted list. Then the problem will be very simple.

``` python
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
```
