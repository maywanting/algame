class Solution(object):
    def sortColors1(self, nums):
        val = [0, 0, 0]
        for v in nums:
            val[v] += 1

        for i in range(val[0]):
            nums[i] = 0

        for i in range(val[1]):
            nums[i+val[0]] = 1

        for i in range(val[2]):
            nums[i+val[1]+val[0]] = 2

        # print(nums)

    def sortColors(self, nums):
        si = 0
        ei = len(nums) - 1
        mi = 0

        while mi <= ei:
            if nums[mi] >


solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))
print(solution.sortColors([2,0,1]))
