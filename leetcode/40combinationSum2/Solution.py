class Solution(object):
    def combinationSum2(self, candidates, target):
        self.canDict = {}
        for val in candidates:
            if val in self.canDict:
                self.canDict[val] += 1
            else:
                self.canDict[val] = 1
        # print(self.canDict)
        self.res = []
        candi = list(set(candidates))
        candi.sort() #remove duplicates and sort
        self.loopcal(candi, target, [], 1)
        return self.res

    def loopcal(self, candidates, target, resList, num):
        # print("(========)")
        # print(candidates)
        # print(target)
        # print(resList)
        # print(num)
        # print("(========)")
        if target == 0:
            self.res += [resList]
            # print("+++++++++")
            # print(resList)
            # print("+++++++++")
            return
        elif target < 0:
            return
        else:
            for i, value in enumerate(candidates):
                # print("-----" + str(value))
                # print(num)
                if num < self.canDict[value]: #still using this candidate
                    self.loopcal(candidates[i:], target - value, resList + [value], num + 1)
                else: #use another candidate
                    self.loopcal(candidates[i+1:], target - value, resList + [value], 1)

                num = 1

solution = Solution()
# print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
# print(solution.combinationSum2([3, 1, 3, 5, 1, 1], 8))
