class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        index1 = length - 2
        for i in range(length - 1):
            if nums[index1] < nums[index1 + 1]:
                break
            index1 -= 1
        #  print(index1)
        #  print(nums)

        if index1 >= 0: # find swap number
            index2 = length - 1
            maxNum = index1 + 1
            for i in range(length - index1 - 1):
                if (nums[index2] > nums[index1]) and (nums[index2] <= nums[index1 + 1]):
                    maxNum = index2
                    break
                index2 -= 1
            print(maxNum)

            temp = nums[index1]
            nums[index1] = nums[maxNum]
            nums[maxNum] = temp
            print(nums)

        flag1, flag2 = index1+1, length-1
        while flag2 > flag1:
            temp = nums[flag2]
            nums[flag2] = nums[flag1]
            nums[flag1] = temp
            flag1, flag2 = flag1+1, flag2-1

        return nums

solution = Solution()
print(solution.nextPermutation([6, 5, 3, 5, 4, 2, 1])) #6 5 4 1 2 3 5
print(solution.nextPermutation([4, 2, 1])) # 1 2 4
print(solution.nextPermutation([1, 2, 3])) # 1 3 2
print(solution.nextPermutation([3, 2, 1])) # 1 2 3
print(solution.nextPermutation([1, 1, 5])) # 1 5 1
print(solution.nextPermutation([1, 3, 2])) # 2 1 3
print(solution.nextPermutation([2, 3, 1, 3, 3])) # 2 3 3 1 3
