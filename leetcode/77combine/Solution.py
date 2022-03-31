class Solution(object):
    def combine(self, n, k):
        self.res = []
        self.dfs([], 1, n, k)
        return self.res

    def dfs(self, nowA, nowS, n, k):
        if k == 0:
            self.res.append(nowA)
        else:
            print(range(nowS, n-k+2))
            for i in range(nowS, n-k+2):
                self.dfs(nowA + [i], i+1, n, k-1)

solution = Solution()
print(solution.combine(4, 2))
print(solution.combine(1, 1))