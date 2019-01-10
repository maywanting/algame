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

solution = Solution()
print(solution.myPow(2.0, 10))
print(solution.myPow(2.1, 3))
print(solution.myPow(2.0, -2))
