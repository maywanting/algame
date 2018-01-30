3Sum Closest
---

# Description

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array `S = {-1 2 1 -4}`, and target = 1.

The sum that is closest to the target is 2. `(-1 + 2 + 1 = 2)`.

# Solution

This problem is similiar with problem 15. So the solution is similiar. What's more, this question is simplier than the last one.

``` python
class Solution(object):
    def getDistance(self, num1, num2):
        distance = num1 - num2
        if distance < 0:
            return -distance
        else:
            return distance

    def threeSumClosest(self, nums, target):
        nums.sort()
        minValue = nums[0] + nums[1] + nums[2]
        minDistance = self.getDistance(target, minValue)

        for i in range(len(nums) - 2):
            newTarget = target - nums[i]
            p, q = i+1, len(nums)-1
            while p < q:
                sumValue = nums[p] + nums[q]
                if sumValue < newTarget:
                    p += 1
                elif sumValue > newTarget:
                    q -= 1
                else:
                    return target

                distance = self.getDistance(sumValue, newTarget)
                if distance < minDistance:
                    minDistance = distance
                    minValue = sumValue + nums[i]

        return minValue
```
