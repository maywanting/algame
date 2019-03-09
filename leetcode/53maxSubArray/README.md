Maximum Subarray
---

# Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Solution

I think the most important thing is to figure out the start of potential substring.

``` python
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        curValue = maxValue = nums[0]
        for value in nums[1:]:
            curValue = max(value, value + curValue)
            maxValue = max(curValue, maxValue)
        return maxValue
```
