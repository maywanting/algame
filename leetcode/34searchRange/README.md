Search for a Range
---

# Description

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return `[-1, -1]`.

For example,

Given `[5, 7, 7, 8, 8, 10]` and target value 8,

return `[3, 4]`.

# Solution

This question is very like the last one. So, the first version of my code is below:

``` python
class Solution(object):
    def searchRange(self, nums, target):
        if target in nums:
            start, i, length = nums.index(target), 1, len(nums)
            while ((start + i) < length) and (nums[start + i] == nums[start]):
                i += 1
            return [start, start + i - 1]
        else:
            return [-1, -1]
```

And is accepted. But, I know that the last problem is aimed at using binary searching. So, I alse write the binary searching version, and is accepted.

``` python
class Solution(object):
    def searchRange(self, nums, target):
        lo, hi, length = 0, len(nums)-1, len(nums)

        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                i, j = 1, 1
                while ((mid - i) >= 0) and (nums[mid - i] == target):
                    i += 1
                while ((mid + j) < length) and (nums[mid + j] == target):
                    j += 1
                return [mid - i + 1, mid + j - 1]

            if (nums[lo] <= target) and nums[mid] > target:
                hi = mid - 1
            else :
                lo = mid + 1

        return [-1, -1]
```
