class Solution(object):
    #  def searchRange(self, nums, target):
        #  if target in nums:
            #  start, i, length = nums.index(target), 1, len(nums)
            #  while ((start + i) < length) and (nums[start + i] == nums[start]):
                #  i += 1
            #  return [start, start + i - 1]
        #  else:
            #  return [-1, -1]

    def searchRange(self, nums, target):
        lo, hi, length = 0, len(nums)-1, len(nums)

        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                i, j = 1, 1
                while ((mid - i) >= 0) and (nums[mid - i] == target):
                    i += 1
                while ((mid + j) < length) and (nums[mid + j] == target):
                    j += 1
                return [mid - i + 1, mid + j - 1]

            if (nums[lo] <= target) and nums[mid] > target:
                hi = mid - 1
            else :
                lo = mid + 1

        return [-1, -1]

solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
print(solution.searchRange([1], 1))
