class Solution(object):
    def removeDuplicates(self, nums):
        p, num = 0, 1

        for q in range(1, len(nums)):
            if nums[p] == nums[q]:
                if num < 2: # p move
                    num += 1
                    p += 1
                    nums[p] = nums[q]
            else: # p move and reset nums
                num = 1
                p += 1
                nums[p] = nums[q]
        print(nums)
        return p+1


solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(solution.removeDuplicates([1,1,1,2,2,3]))
