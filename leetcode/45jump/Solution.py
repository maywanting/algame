import time
class Solution(object):
    def jump(self, nums):
        length = len(nums)
        minJump = [i for i in range(length)]

        jump = p = q = 0
        while q < length:
            # print(minJump)
            end = p + nums[p] + 1
            if end >= length:
                return min(minJump[length-1], minJump[p]+1)

            for i in range(q, end):
                minJump[i] = min(minJump[i] , minJump[p]+1)
            q = max(q, end)
            p += 1

solution = Solution()
start = time.time()
# print(solution.jump([2, 3, 1, 1, 4])) # 2
# print(solution.jump([6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3])) #4
# print(solution.jump([0])) #0
print(solution.jump([9,4,5,4,1,8,1,2,0,7,8,7,0,6,6,1,1,2,5,0,9,8,4,7,9,6,8,1,4,0,8,5,5,3,9,8,1,2,2,3,0,1,3,2,7,9,3,0,1]))
end = time.time()
print(end - start)
# print(solution.jump([2, 1]))
