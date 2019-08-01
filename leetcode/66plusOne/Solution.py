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

solution = Solution()
print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([9, 9, 9, 9]))
