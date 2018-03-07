Divide Two Integers
---

# Description

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

# Solution

The first solution I have thought is to using divisor to minus dividend until the dividend is smaller than divisor, the minusing times is the result. Divide is defined as that. But, there is a better solution to solve this problem.

We can use bit manipulation to solve this question. So the time complexity is O((log N)^2)

``` python
class Solution(object):
    def divide(self, dividend, divisor):
        # max num
        if (divisor == 0 or (dividend == -2147483648 and divisor == -1)):
            return 2147483647

        # positive sign
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result, tempRes = 0, 1
        while dividend >= divisor:
            tempDivisor, tempRes = divisor, 1
            while (dividend - tempDivisor) >= tempDivisor:
                tempDivisor <<= 1
                tempRes <<= 1
            result += tempRes
            dividend -= tempDivisor

        return -result if sign else result
```
