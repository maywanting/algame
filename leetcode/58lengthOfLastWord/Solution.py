class Solution(object):
    def lengthOfLastWord(self, s):
        strArr = s.split()
        if len(strArr) < 1:
            return 0
        else:
            return len(strArr[-1])

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("HelloWorld"))
