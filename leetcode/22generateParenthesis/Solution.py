class Solution(object):
    def generateParenthesis(self, n):
        self.res = []
        self.num = n
        self.getParenth('', 0, 0)
        return self.res

    def getParenth(self, string, left, right):
        if len(string) == self.num * 2:
            self.res.append(string)

        if right < self.num:
            self.getParenth(string + "(", left, right + 1)
        if left < right:
            self.getParenth(string + ")", left + 1, right)

solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
