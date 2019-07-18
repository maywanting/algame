class Solution(object):
    def isNumber(self, s):
        try:
            res = float(s)
            return True
        except:
            return False

solution = Solution()
print(solution.isNumber("0"))
print(solution.isNumber(" 0.1"))
print(solution.isNumber("abc"))
print(solution.isNumber("1 a"))
print(solution.isNumber("2e10"))
print(solution.isNumber(" -90e3"))
print(solution.isNumber(" 1e"))
print(solution.isNumber("e3"))
print(solution.isNumber("6e-1"))
