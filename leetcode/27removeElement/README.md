Remove Element
---

# Description

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example: Given nums = `[3,2,2,3]`, val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

# Something about In-place Algorithm

What is In-place Algorithm? In wiki, words below are found:

>In computer science, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure. However a small amount of extra storage space is allowed for auxiliary variables. The input is usually overwritten by the output as the algorithm executes.

In another word, the algorithm will return the ouput by modify the input, other than using 'return'.

# Solution

......

No comment

``` python
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
```
