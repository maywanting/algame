class Solution(object):
    def threeSum(self, nums):
        nums.sort()

        resultArray = []
        length = len(nums)
        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]: #same number will be passed
                continue

            target = -nums[i]
            j, k = i+1, length-1
            while j < k:
                if (nums[j] + nums[k]) == target: #reach the target
                    resultArray.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1
                    while j < length and nums[j] == nums[j - 1]:
                        j += 1

                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1

                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return resultArray


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) #[[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0, 0, 0]))
