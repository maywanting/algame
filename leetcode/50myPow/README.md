Pow(x, n)
---

# Description
Implement pow(x, n), which calculates x raised to the power n (x<sub>n</sub>).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

# Solution

We all know that x<sub>n</sub> = x * x * x * x ...... and the number of x is n

So the simplest solution is using 'for' loop. But this will cause 'Time Limit Exceeded'. So how to solve it?

For simplest description, n = 10. So, x<sub>10</sub> = x<sub>5</sub> * x<sub>5</sub>, x<sub>5</sub> = x<sub>2</sub> * x<sub>2</sub> * x, x<sub>2</sub> = x * x;

So, when n is odd, x<sub>n</sub> = x<sub>n/2</sub> * x<sub>n/2</sub> * x. when n is even, x<sub>n</sub> = x<sub>n/2</sub> * x<sub>n/2</sub>

``` python
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = 0 - n
        return self.loopPow(x, n)

    def loopPow(self, x, n):
        if (n == 1):
            return x
        half = self.loopPow(x, n/2)
        if (n % 2) == 1: #odd
            return half*half*x
        if (n % 2) == 0: #even
            return half*half
```
