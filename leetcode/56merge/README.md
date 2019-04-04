Merge Intervals
---

# Description

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Solution

First, sort the list of intervals based on the start item in interval. Then merge the intervals according to the rule: if intervals[i].end is smaller than or equal with intervals[i-1].start, then intervals[i] and intervals[i-1] can be merged.

``` python
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
```

---

# Description

# Solution

