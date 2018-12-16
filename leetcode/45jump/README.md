Jump Game II
---

# Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.

# Solution

Actually, I can not catch the meaning of this question. After I finish the '55.Jump Game', I just know the meaning of this problem.

To solve this problem, we need to know one thing: if we set an array D to represent minimum jump length, D[i+1] >= D[i]

So, we just need two pointer. Pointer1 records the jump item, Pointer2 records the refreshing item of mininum nunber of jumps. So, D[P1:P2] = min(D[P1:P2], D[P1]+1)

So, when the D[length - 1] is refreshed, we can get the result, and the result is D[length - 1]

``` python
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
```
