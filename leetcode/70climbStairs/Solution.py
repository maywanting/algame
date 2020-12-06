class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        l1 = 1
        l2 = 1
        l = 2
        for i in range(n-1):
            l = l1 + l2
            l1 = l2
            l2 = l
        return l

solution = Solution()
print(solution.climbStairs(2)) #2
print(solution.climbStairs(3)) #3
print(solution.climbStairs(10)) #89

