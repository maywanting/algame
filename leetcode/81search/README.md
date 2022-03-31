Search in Rotated Sorted Array II
---

# Description

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    nums is guaranteed to be rotated at some pivot.
    -104 <= target <= 104

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

# Solution

Binary search in one of the best solution to solve the searching problem in this sorted array.

In this problem, the sorted array has some special conditions. So Boolean expression for binary search is more complex than usual.

There are searching pointer, `l` means the first num of search range, while `r` means the end num of search range. 

1. `nums[l] >= nums[r]` : means the pivot index is in this area. Continue to serch.
2. `nums[l] < nums[r]` : the nums in this array is in non-decreasing order. So, if the value of target is within this area, Continue to search. Otherwise, the target is not in this area, return False.

So, based on these judgements, the problem can be solved.

``` python
class Solution(object):
    def binsearch(self, nums, l, r, t):
        if (nums[l] == t) or (nums[r] == t):
            return True

        if l>=r :
            return False

        if (nums[l] < nums[r]) and (t > nums[r] or t < nums[l]):
            return False

        m = (l+r) / 2
        return self.binsearch(nums, l, m, t) or self.binsearch(nums, m+1, r, t)

    def search(self, nums, target):
        return self.binsearch(nums, 0, len(nums)-1, target)
```

