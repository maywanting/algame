class Solution(object):
    def binsearch(self, nums, l, r, t):

        if (nums[l] == t) or (nums[r] == t):
            return True

        if l>=r :
            return False

        if (nums[l] < nums[r]) and (t > nums[r] or t < nums[l]):
            return False

        m = (l+r) / 2
        return self.binsearch(nums, l, m, t) or self.binsearch(nums, m+1, r, t)

    def search(self, nums, target):
        return self.binsearch(nums, 0, len(nums)-1, target)
        
solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 0))
print(solution.search([2,5,6,0,0,1,2], 3))
print(solution.search([2,5,6,0,0,1,2], 8))
print(solution.search([2,5,6,0,0,1,2], 1))
print(solution.search([2,5,6,0,0,1,2], -1))
