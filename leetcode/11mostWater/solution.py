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

solution = Solution()
print(solution.maxArea([1, 1]))
