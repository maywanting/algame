class Solution(object):
    def permute(self, nums):
        self.res = []
        self.loopPer([], nums)
        return self.res

    def loopPer(self, pre, sub):
        print(pre)
        print(sub)
        print("=========")
        if len(sub) == 1:
            print("add")
            self.res += [pre + sub]
            print(self.res)
            return
        for index, item in enumerate(sub):
            self.loopPer(pre + [item], sub[:index] + sub[index+1:])

solution = Solution()
print(solution.permute([1, 2, 3, 4]))
