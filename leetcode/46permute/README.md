Permutations
---

# Description
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

# Solution

This is a math problem about Arrangement, and I still remember the math equation is

A<sub>n</sub><sup>m</sup> = n! / (n-m)!

This question is the situation about m = n.

I use DFS algorithm to solve this question.

``` python
class Solution(object):
    def permute(self, nums):
        self.res = []
        self.loopPer([], nums)
        return self.res

    def loopPer(self, pre, sub):
        if len(sub) == 1:
            self.res += [pre + sub]
            return
        for index, item in enumerate(sub):
            self.loopPer(pre + [item], sub[:index] + sub[index+1:])
```
