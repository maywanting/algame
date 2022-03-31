Subsets
---

# Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

# Solution

This question is similar with the last one, and easier than that. We also use DFS to solve this quiz.

``` python
class Solution(object):
    def dfs(self, now, nums):
        self.res.append(now)
        if len(nums) == 0:
            return
        else:
            for i, v in enumerate(nums):
                self.dfs(now+[v], nums[i+1:])

    def subsets(self, nums):
        self.res = []
        self.dfs([], nums)
        return self.res
```