class Solution(object):
    def firstMissingPositive(self, nums):
        numSet = set(nums)
        item = 1
        while True:
            if item not in numSet:
                return item
            else:
                item += 1

solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))
print(solution.firstMissingPositive([3, 4, -1, 1]))
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
