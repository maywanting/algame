class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        #  print(len(s))

        validArray = [0 for i in range(len(s))]
        if s[0:2] == '()':
            validArray[1] = 2
        for i in range(2, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                validArray[i] = validArray[i-2] + 2
            if s[i] == ')' and s[i-1] == ')':
                front = i - validArray[i-1] - 1
                if front >= 0 and s[front] == '(':
                    validArray[i] = validArray[i-1] + 2
                    if (front-1) >= 0:
                        validArray[i] += validArray[front-1]

        #  print(validArray)
        return max(validArray)

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
