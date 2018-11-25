class Solution(object):
    def isMatch(self, s, p):
        s = '$' + s
        p = '$' + p
        matchMatrix = [[False for j in range(len(s))] for i in range(len(p))]
        matchMatrix[0][0] = True
        for i in range(1, len(p)):
            if (p[i] == '*'):
                matchMatrix[i][0] = matchMatrix[i-1][0]

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == '*': # uncertain number of character match
                    if matchMatrix[i-1][j] or matchMatrix[i][j-1] or matchMatrix[i-1][j-1]:
                        matchMatrix[i][j] = True
                elif p[i] == '?' or p[i] == s[j]: # single character match
                    matchMatrix[i][j] = matchMatrix[i-1][j-1]
        # print(matchMatrix)
        return matchMatrix[len(p) - 1][len(s) - 1]

solution = Solution()
print(solution.isMatch('acdcb', 'a*c?b')) #false
print(solution.isMatch('aa', 'a')) #false
print(solution.isMatch('aa', '*')) #true
print(solution.isMatch('cb', '?a')) #false
print(solution.isMatch('acdcb', '*a*b')) #true
print(solution.isMatch('aab', 'c*a*b')) #false
