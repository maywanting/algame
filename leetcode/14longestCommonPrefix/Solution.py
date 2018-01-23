class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = "" if (len(strs) is 0) else strs[0]
        for i in range(1, len(strs)):
            current = strs[i]
            for j in range(len(current)):
                if j >= len(longest) or longest[j] != current[j]:
                    j -= 1
                    break
            longest = "" if (len(current) is 0) else longest[:j+1]
        return longest

solution = Solution()
#  print(solution.longestCommonPrefix([]))
print(solution.longestCommonPrefix(["abc", "ab", "abccc"])) #ab
print(solution.longestCommonPrefix(["abc", "abccds", "abccc"])) #abc
print(solution.longestCommonPrefix(["abc", "abdcds", "abccc"])) #ab
#  print(solution.longestCommonPrefix(["", ""])) #""
