Plus One
---

# Description

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

# Solution

I think this question is too simple.

``` python
class Solution(object):
    def plusOne(self, digits):
        res = 0
        for i in digits:
            res = res * 10 + i
        res += 1
        resArr = []
        while res > 0:
            resArr = [res % 10] + resArr
            res /= 10
        return resArr

```
