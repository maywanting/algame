Valid Parentheses
---

# Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Solution

This problem is a typical example about using Stack. I have learned it from the Data-Structures class in my university.

``` python
class Solution(object):
    bracketsMap = {
        '(': 1,
        ')': -1,
        '[': 2,
        ']': -2,
        '{': 3,
        '}': -3,
    }

    def isValid(self, s):
        justifyArray = []
        for i in range(len(s)):
            length = len(justifyArray)
            currentValue = self.bracketsMap[s[i]]
            if length > 0:
                if (justifyArray[length - 1] + currentValue) == 0:
                    justifyArray.pop()
                else:
                    justifyArray.append(currentValue)
            else:
                justifyArray.append(currentValue)
        #  print(justifyArray)
        return len(justifyArray) == 0

```
