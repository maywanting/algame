class Solution(object):
    def threeSum(self, nums):
        hashNum = {}
        id = 0
        for i in range(len(nums)):
            if hashNum.has_key(nums[i]):
                hashNum[nums[i]][0] += 1
            else:
                hashNum[nums[i]] = [1, id]
                id += 1

        print(hashNum)
        result = []
        for i, value1 in enumerate(hashNum):
            if hashNum[value1][0] > 1: #same result
                if value1 is 0 and hashNum[value1][0] > 2:
                    result.append([0, 0, 0])
                else:
                    res = - (value1 * 2)
                    if hashNum.has_key(res) and hashNum[value1][1] < hashNum[res][1]:
                        result.append([value1, value1, res])

            for j, value2 in enumerate(hashNum):
                if j <= i:
                    continue

                res = - value1 - value2
                if hashNum.has_key(res) and res != value1 and res != value2 and hashNum[value2][1] < hashNum[res][1]: # meet the requirement
                    result.append([value1, value2, res])

        return result

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
