class Solution(object):
    def sortColors(self, nums):
        val = [0, 0, 0]
        for v in nums:
            val[v] += 1

        return val

solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))
