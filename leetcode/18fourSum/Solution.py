class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        resultArray = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: #same number
                continue

            current1 = nums[i]
            target1 = target - current1
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: #same number
                    continue

                current2 = nums[j]
                target2 = target1 - current2
                p, q = j+1, len(nums) - 1
                while p < q:
                    if (nums[p] + nums[q]) == target2:
                        resultArray.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1
                        while p < len(nums) - 1 and nums[p] == nums[p - 1]:
                            p += 1
                        while q > j + 1 and nums[q] == nums[q + 1]:
                            q -= 1
                    elif nums[p] + nums[q] > target2:
                        q -= 1
                    else:
                        p += 1
        return resultArray

solution = Solution()
#  print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
#  print(solution.fourSum([0, 0, 0, 0], 0))
print(solution.fourSum([0, 4, -5, 2, -2, 4, 2, -1, 4], 12))
