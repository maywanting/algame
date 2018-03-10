Next Permutation
---

# Description

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

# Solution

First time, I really don't know what does this probelm want to do. So, after explanation from someone's discussion, I just understand what this problem means.

When we get all combinations of some numbers, the right process may this, for example:

If the numbers are `1, 2, 3, 4`

```
1- 1 2 3 4
2- 1 2 4 3
3- 1 3 2 4
4- 1 3 4 2
5- 1 4 2 3
6- 1 4 3 2
7- 2 1 3 4
8- 2 1 4 3
9- 2 3 1 4
10- 2 3 4 1
11- 2 4 1 3
12- 2 4 3 1
13- 3 1 2 4
14- 3 1 4 2
15- 3 2 1 4
16- 3 2 4 1
17- 3 4 1 2
18- 3 4 2 1
19- 4 1 2 3
20- 4 1 3 2
21- 4 2 1 3
22- 4 2 3 1
23- 4 3 1 2
24- 4 3 2 1
```

So, why we so combine the numbers? the reason is the combination number is also sorted. You may not find another combination number which is smaller than No.12 and bigger than N0.11.

According to the problem, if the input combination number is No.11, the output should be No.12. If the input combination number is No.24, the output is No.1.

So, the algorithm of combinations is the most important thing.

``` python
class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        index1 = length - 2
        for i in range(length - 1):
            if nums[index1] < nums[index1 + 1]:
                break
            index1 -= 1

        if index1 >= 0: # find swap number
            index2 = length - 1
            maxNum = index1 + 1
            for i in range(length - index1 - 1):
                if (nums[index2] > nums[index1]) and (nums[index2] <= nums[index1 + 1]):
                    maxNum = index2
                    break
                index2 -= 1

            temp = nums[index1]
            nums[index1] = nums[maxNum]
            nums[maxNum] = temp

        flag1, flag2 = index1+1, length-1
        while flag2 > flag1:
            temp = nums[flag2]
            nums[flag2] = nums[flag1]
            nums[flag1] = temp
            flag1, flag2 = flag1+1, flag2-1
```
