class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        curValue = maxValue = nums[0]
        for value in nums[1:]:
            curValue = max(value, value + curValue)
            maxValue = max(curValue, maxValue)
        return maxValue

    def maxSubArray2(self, nums):
        maxRes = sumV = last = 0
        for value in nums:
            # print("--------")
            # print(last)
            # print(sumV)
            # print(value)
            if value * sumV < 0:
                last += sumV
                if sumV > 0:
                    if last > maxRes: #refresh
                        maxRes = last
                else:
                    if last < 0:
                        last = 0
                sumV = value
            else: #same sign sum
                sumV += value
        if sumV > maxRes:
            maxRes = sumV
        return maxRes

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,7]))
print(solution.maxSubArray([-2,5,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([-1])) #-1
