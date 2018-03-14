Search in Rotated Sorted Array
---

# Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

# Solution

In fact, my first accepted solution is below

``` python
class Solution(object):
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1
```

I was confused that why this problem is so easy and the difficult level is medium. After reading the discussion, I understand this problem should use binary search.

``` python
class Solution(object):
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo + hi) / 2
            print(mid)
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
```
