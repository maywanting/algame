class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.process(candidates, [], target)
        return self.res

    def process(self, candinates, resList, target):
        if target == 0:
            self.res = [resList] + self.res
            return
        else:
            for item in range(len(candinates)-1, -1, -1):
                if ((target - candinates[item]) >= 0):
                    self.process(candinates[:item+1], [candinates[item]] + resList, target - candinates[item])

solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
print(solution.combinationSum([2, 3, 5], 8))
