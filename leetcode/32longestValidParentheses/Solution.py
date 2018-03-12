class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) <= 1:
            return 0

        #  for i in range(1, length):
        i, nums, j= 1, [0], 0
        while i < len(s):
            if (s[i] == ')') and (s[i-1] == '('):
                s = s[:i-1] + s[i+1:]
                #  print(s)
                i -= 1
                nums[j] += 2
            elif (s[i] == '(') and (i+1 < len(s)) and (s[i+1] == ')'):
                s = s[:i] + s[i+2:]
                #  print(s)
                nums[j] += 2
            else:
                if nums[j] != 0:
                    s = s[:i] + 'N' + s[i:]
                    i, j = i+2, j+1
                    nums.append(0)
                else:
                    i += 1

        if nums[j] != 0:
            s = s[:i] + 'N' + s[i:]
        print(s)
        print(nums)

        res, maxRes, j = 0, 0, 0
        for i in range(len(s)):
            if s[i] == 'N':
                res += nums[j]
                j += 1
            else:
                if maxRes < res:
                    maxRes = res
                res = 0

        if maxRes < res:
            maxRes = res
        return maxRes

solution = Solution()
print(solution.longestValidParentheses(")()())")) #4
print(solution.longestValidParentheses(")(()()))()")) #6
print(solution.longestValidParentheses(")(()))()(())")) #6
print(solution.longestValidParentheses(")()())()")) #4
print(solution.longestValidParentheses("(()")) #2
print(solution.longestValidParentheses(")(")) #0
print(solution.longestValidParentheses("()")) #2
print(solution.longestValidParentheses("()(())")) #6
print(solution.longestValidParentheses(")(((((()())()()))()(()))(")) #22
