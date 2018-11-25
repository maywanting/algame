Wildcard Matching
---

# Description

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


# Solution

This question is similiar with the Q.10. The content of Q.10 is '.' and '*'. This time '?' and '*' is contained.

Comparised with the regular expression, '*' in this problem is '.*', '?' is '.'. So, dealing this question likes Q.10, matchMatirx is required.

For describing easily, I settle this:

```
A1 | A2
A3 | A4:need to justify
```

In above matrix, A4 is needed to justify according to A1 or A2 or A3 according to the pattern characters.

When matching with '*', A4 will be true when A1 or A2 or A3 whichever is true. A1 true means '*' matches any one character. A3 means number of characters id two or more. A2 means there is no matching character.

Also, this is difficult to deal with the head of string. '$' is added in string and pattern to be dealt with easily.


``` python
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
        return matchMatrix[len(p) - 1][len(s) - 1]
```
