class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        nums.sort()
        self.dfs([], nums)
        return self.res

    def dfs(self, pre, sub):
        if len(sub) == 1:
            self.res += [pre + sub]
            return

        for i in range(len(sub)):
            if (i == 0) or (sub[i-1] != sub[i]):
                self.dfs(pre + [sub[i]], sub[:i] + sub[i+1:])

solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
print(solution.permuteUnique([1, 1, 2, 2]))
print(solution.permuteUnique([1, 2, 3]))
print(solution.permuteUnique([3, 3, 0, 3]))
