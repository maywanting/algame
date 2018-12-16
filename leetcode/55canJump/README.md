Jump Game
---

# Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Solution

We can use greedy algorithm to solve this question. We need to know that why can not able to reach the last index. The reason, all of the maximum jump can not over zero point. So we search the array, and calculate the maximum jump of this item. If the maximun jump is smaller or equal item id, this means we can not jump over this point any way.

``` pythen
class Solution(object):
    def canJump(self, nums):
        lastMax = nums[0]
        for i in range(1, len(nums)):
            if (lastMax <= i-1):
                return False
            lastMax = max(lastMax, i + nums[i])
        return lastMax >= len(nums)-1
```
