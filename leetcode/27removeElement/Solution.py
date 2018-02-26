class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))
