Implement strStr()
---

# Description

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

## Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

# Solution

This problem is a string pattern problem. I think the best solution to solve this problem is using KMP algorithm. But, it seems that KMP algorithm is not needed, simple algorithm is alse accepted.

``` python
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```
