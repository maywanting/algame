Regular Expression Matching
---

# Description

Implement regular expression matching with support for '.' and '*'.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```

# Solution

I think this problem is very difficult to me. I spend a lot of time on dealing with it.

This problem seems like Regular Expression Matching but only two characters are needed to consider. The first thing needed to do is understand the pattern. So I transfer pattern string to be the understandable array. first is the matching-character, second is the remark of '*', called number-character.

For describing easily, I settle this:

```
(0, 0) | (0, 1)
(1, 0) | need to justify
```

So, when matching, both matching-character and number-character needed to be considered. if number-character is 0 and matching-character is right, it is enough that we just consider the front character is matched, for another words, just see the value in (0,0)

if number-character is true, it means, this number can be 0, 1, and more. 0 means this can be ignored, for another word, just consider the (0, 1). 1 means consider the front character is matched, just consider the (0, 0). more means just see (1, 0)

I think it is difficult to deal with the begin and if the first pattern is number-character type. So I add the '$' to mark the start, while '$' means the end of string in the Regular Expression Matching.

``` Python
class Solution(object):
    def changeP(self, p):
        res = [['$', 0]] # start mark
        j = 1
        for i in range(len(p)):
            if p[i] == '*':
                res[j-1][1] = 1
            else :
                res.append([p[i], 0])
                j += 1
        return res

    def isMatch(self, s, p):
        pArray = self.changeP(p)
        s = '$' + s
        flag = [[False for col in range(len(s))] for row in range(len(pArray))]
        flag[0][0] = True
        for i in range(1, len(pArray)):
            for j in range(len(s)):
                if (s[j] is pArray[i][0]) or (pArray[i][0] == '.' and s[j] != '$'): # match
                    if pArray[i][1] : # *type
                        flag[i][j] = flag[i-1][j-1] or flag[i-1][j] or flag[i][j-1]
                    else: # simple type
                        flag[i][j] = flag[i-1][j-1]
                else: # not match
                    if pArray[i][1]:  #*type
                        flag[i][j] = flag[i-1][j]
        return flag[len(pArray)-1][len(s)-1]
```
