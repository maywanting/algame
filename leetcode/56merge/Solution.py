class Solution(object):
    def merge(self, intervals):
        length = len(intervals)
        if length == 0:
            return []
        intervals.sort(key=lambda interval: interval.start)
        #print(intervals[0].start)
        res = [intervals[0]]
        for i in range(1, length):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res += [intervals[i]]
        return res

solution = Solution()
# print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solution.merge([[1,4],[0,4]]))
class Solution(object):
    def merge(self):

solution = Solution()
print(solution.merge())
