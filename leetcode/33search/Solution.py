class Solution(object):
    #  def search(self, nums, target):
        #  if target in nums:
            #  return nums.index(target)
        #  else:
            #  return -1

    def search(self, nums, target):
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo + hi) / 2
            print(mid)
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

solution = Solution()
#  print(solution.search([4, 5, 6, 7, 0, 1, 2], 5))
#  print(solution.search([], 5))
print(solution.search([3, 1], 3))
