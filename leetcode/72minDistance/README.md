Edit Distance
---

# Description
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```
Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

# Solution

This is a DP problem. I think the main solution is create a storage arrage DP. The size of this DP arrage is (len(word1) + 1, len(word2) + 1). So the meaning of the element DP[i][j] is that, we need at least DP[i][j] steps when convert word1[:i-1] to word2[:j-1].

According to the description, there are three operations to convert the string. If word1[i] == word2[j], there is no need to do the operation, DP[i][j] = DP[i-1][j-1]. Otherwise, we need to perfom the operation of the I(insert), D(delete), R(replace).

```
Replace operation | Delete operation
Insert operation  | DP[i][j]
```

So the value of DP[i][j] is equal to 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])

``` python
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
```
