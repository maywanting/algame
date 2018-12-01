class Solution(object):
    def canJump(self, nums):
        lastMax = nums[0]
        for i in range(1, len(nums)):
            if (lastMax <= i-1):
                return False
            lastMax = max(lastMax, i + nums[i])
        return lastMax >= len(nums)-1

solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4])) # True
print(solution.canJump([3, 2, 1, 0, 4])) # false
print(solution.canJump([1])) # True
print(solution.canJump([2, 0])) # True
print(solution.canJump([0])) # True
