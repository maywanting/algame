class Solution(object):
    def getDistance(self, num1, num2):
        distance = num1 - num2
        if distance < 0:
            return -distance
        else:
            return distance

    def threeSumClosest(self, nums, target):
        nums.sort()
        minValue = nums[0] + nums[1] + nums[2]
        minDistance = self.getDistance(target, minValue)

        for i in range(len(nums) - 2):
            newTarget = target - nums[i]
            p, q = i+1, len(nums)-1
            while p < q:
                sumValue = nums[p] + nums[q]
                if sumValue < newTarget:
                    p += 1
                elif sumValue > newTarget:
                    q -= 1
                else:
                    return target

                distance = self.getDistance(sumValue, newTarget)
                if distance < minDistance:
                    minDistance = distance
                    minValue = sumValue + nums[i]

        return minValue

solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1)) #2
print(solution.threeSumClosest([0, 0, 0], 1)) #0
