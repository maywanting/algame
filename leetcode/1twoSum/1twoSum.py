#!/usr/bin/env python
# encoding: utf-8

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

solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
