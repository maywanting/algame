Generate Parentheses
---

# Description

 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 For example, given n = 3, a solution set is:

 ```
 [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
 ]
 ```

# Solution

So, when I try to solve this question, I draw a tree to find the rule. So, when the loop number depends on conditions, recursive is a good method to solve.

``` python
class Solution(object):
    def generateParenthesis(self, n):
        self.res = []
        self.num = n
        self.getParenth('', 0, 0)
        return self.res

    def getParenth(self, string, left, right):
        if len(string) == self.num * 2:
            self.res.append(string)

        if right < self.num:
            self.getParenth(string + "(", left, right + 1)
        if left < right:
            self.getParenth(string + ")", left + 1, right)
```
