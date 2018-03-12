Longest Valid Parentheses
---

# Description

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Solution

We can use dynamical programming to solve this problem. So, an array `validArray` is to record the valid substring length and ith means the length of valid substring length ending by ith. Notice, the valid substring must include the ith element.

So, when element is `(`, the value is always 0. When emelemt is ')', the value will be depended by the element before ith.

- if validArray[i-1] is `(`

`validArray[i] = validArray[i-2] + 2` when (i-2)th element exists.

- if validArray[i-1] id `)`

So, the `(` which pairs to ith should be in (i - validArray[i-1] - 1)th. If the pair one is '('

`validArray[i] = validArray[i-1] + 2 + validArray[i-validArray[i-1]-2]`

``` python
class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0

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
        return max(validArray)
```
