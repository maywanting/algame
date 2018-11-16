First Missing Positive
---

# Description

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

```
Input: [1,2,0]
Output: 3
```

Example 2:

```
Input: [3,4,-1,1]
Output: 2
```

Example 3:

```
Input: [7,8,9,11,12]
Output: 1
```

Note:

Your algorithm should run in O(n) time and uses constant extra space.

# Solution

I can not believe that the difficulty of this problem is hard.... So simple.

Just start loop from 1 and find each positive number existed in the supported array. To find more fast, tranform array to set.

``` python
class Solution(object):
    def firstMissingPositive(self, nums):
        numSet = set(nums)
        item = 1
        while True:
            if item not in numSet:
                return item
            else:
                item += 1
```
