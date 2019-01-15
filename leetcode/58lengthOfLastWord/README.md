Length of Last Number
---

# Description

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

# Solution

Split function in python can solve everything.

``` python
class Solution(object):
    def lengthOfLastWord(self, s):
        strArr = s.split()
        if len(strArr) < 1:
            return 0
        else:
            return len(strArr[-1])
```

