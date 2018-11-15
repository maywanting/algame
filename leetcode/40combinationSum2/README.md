Combination Sum II
---

# Description
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

# Solution

This question is a little different with the last one. The differences is that diplication exists and is limited.

So, the first thing in my solution is to make sure the diplication times of earch item and get the undiplicate list.

So above the solution of last question, in each loop should add the diplication time.

``` python
class Solution(object):
    def combinationSum2(self, candidates, target):
        self.canDict = {}
        for val in candidates:
            if val in self.canDict:
                self.canDict[val] += 1
            else:
                self.canDict[val] = 1
        self.res = []
        candi = list(set(candidates))
        candi.sort() #remove duplicates and sort
        self.loopcal(candi, target, [], 1)
        return self.res

    def loopcal(self, candidates, target, resList, num):
        if target == 0:
            self.res += [resList]
            return
        elif target < 0:
            return
        else:
            for i, value in enumerate(candidates):
                if num < self.canDict[value]: #still using this candidate
                    self.loopcal(candidates[i:], target - value, resList + [value], num + 1)
                else: #use another candidate
                    self.loopcal(candidates[i+1:], target - value, resList + [value], 1)
                num = 1
```
