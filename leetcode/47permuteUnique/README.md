Permutations II
---

# Description

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

# Solution

The main solution is similar with the last question's. There is one point needed to be noted. While loop the array to create new node, number repeated again should not be the node.

In my programme, I make sure the unrepeatability by nums[i] != nums[i-1] after sorting the nums.

``` python
class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        nums.sort()
        self.dfs([], nums)
        return self.res

    def dfs(self, pre, sub):
        if len(sub) == 1:
            self.res += [pre + sub]
            return

        for i in range(len(sub)):
            if (i == 0) or (sub[i-1] != sub[i]):
                self.dfs(pre + [sub[i]], sub[:i] + sub[i+1:])
```
