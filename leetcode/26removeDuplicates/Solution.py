class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))
