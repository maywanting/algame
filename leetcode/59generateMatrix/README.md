Spiral Matrix II
---

# Description

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

# Solution

This is a reverse problem of Q54. So, my solution is to implement the spiral order:right, down, left, up. Identification of the border is also important. In this case, we just ensure the next should be zero and the next is not the border of real matrix.

``` python
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
```
