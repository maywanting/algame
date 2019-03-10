Spiral Matrix
---

# Description

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Solution

I think the most important point is identify the border of each loop

``` python
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

            #down
            for i in range(k+1, n-1+k):
                res += [matrix[i][m-1+k]]

            #left
            res += matrix[n-1+k][::-1][k:m+k]

            #up
            for j in range(n-2+k, k, -1):
                res += [matrix[j][k]]
            n -= 2
            m -= 2
            k += 1

        if n == 1: #right
            res += matrix[k][k:m+k]
        elif m == 1: #down
            for i in range(k, n+k):
                res += [matrix[i][m-1+k]]
        return res
```
