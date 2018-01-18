Container With Most Water
---

# Description
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

# Solution

I think this question describtion is very terrible because even if the return result has not been described.

So the question is to find two number ai and aj in an array, to get the biggest result of `abs(j-i)*min(ai, aj)`

``` python
class Solution(object):
    def maxArea(self, height):
        length = len(height)
        maxValue, high, low = 0, length - 1, 0
        while high > low:
            maxValue = max(maxValue, (high - low) * min(height[high], height[low]))
            if height[high] > height[low]:
                low += 1
            else:
                high -= 1

        return maxValue
```
