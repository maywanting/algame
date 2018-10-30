Combination Sum
---

# Description

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

# Solution

I think this is also a tree traversing problem. It can be solved by using tree structure. In this tree, node is the target, and the edge is the item in candidates in earch loop.

there are three processing according to the result that target minus item in earch loop.

- equal to zero: res list meets the requirement
- smaller than zero: res list does not meet the requirement, skip to last node and start next loop
- bigger than zero: still under judgement, minus next item and start next loop

Any tree structure problem can be solved by recursion.

``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.process(candidates, [], target)
        return self.res

    def process(self, candinates, resList, target):
        if target == 0:
            self.res = [resList] + self.res
            return
        else:
            for item in range(len(candinates)-1, -1, -1):
                if ((target - candinates[item]) >= 0):
                    self.process(candinates[:item+1], [candinates[item]] + resList, target - candinates[item])
```
