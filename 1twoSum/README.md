Two Sum
---

# Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Examples

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

# Solution

I think the most important thing of this problem is to save time. Time will be wasted when searching the proper number to meet the aimed one. So i make the number to be the hash key. Hash key will be faster to search for the left number.

I use Python to solve this question.

``` Python
class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        numDic = {}
        for index in range(length):
            numDic[nums[index]] = index

        for index in range(length):
            left = target - nums[index]
            if (numDic.has_key(left)):
                if (numDic[left] == index):
                    continue
                else:
                    return [index, numDic[left]]
        return [index-1, index]
```

