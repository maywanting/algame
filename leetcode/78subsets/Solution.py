class Solution(object):
    def dfs(self, now, nums):
        self.res.append(now)
        if len(nums) == 0:
            return
        else:
            for i, v in enumerate(nums):
                self.dfs(now+[v], nums[i+1:])

    def subsets(self, nums):
        self.res = []
        self.dfs([], nums)
        return self.res

solution = Solution()
print(solution.subsets([1, 2, 3]))
