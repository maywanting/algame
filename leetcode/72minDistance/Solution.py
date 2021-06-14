class Solution(object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]

        # init
        dp[0][0] = 0
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(len1):
            for j in range(len2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])

        # print(dp)
        return dp[-1][-1]

solution = Solution()
# print(solution.minDistance("horse", "ros"))
print(solution.minDistance("intention", "execution"))
