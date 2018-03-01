class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))
print(solution.searchInsert([1, 3, 5, 6], 2))
print(solution.searchInsert([1, 3, 5, 6], 7))
print(solution.searchInsert([1, 3, 5, 6], 0))
