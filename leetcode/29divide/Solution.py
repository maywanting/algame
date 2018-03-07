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

            #  print(tempRes)
            result += tempRes
            dividend -= tempDivisor

        return -result if sign else result

solution = Solution()
print(solution.divide(18, 5))
print(solution.divide(0, 1))
print(solution.divide(2, 0))
print(solution.divide(-1, 1))
print(solution.divide(-1, -1))
print(solution.divide(1, -1))
print(solution.divide(1, 1))
