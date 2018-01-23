Longest Common Prefix
---

# Description

Write a function to find the longest common prefix string amongst an array of strings. 

# Solution

This question is very easy. Only one thing should be noticed is when the length of string is 0.

``` Python
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
```
