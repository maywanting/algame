Climbing Stairs
---

# Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

# Solution

There are two choices for the first step: 1 step and 2 steps. In the case of 1 step, the next steps is same that we take n-1 steps. In the case of 2 steps, the next steps is the same as n-2 steps.

So we can gain the rules:

f(0) = 1
f(1) = 1
f(2) = f(0) + f(1)
f(n) = f(n-1) + f(n-2)

And, the program is very simple

``` python
class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
```

However, there is a missing in this program. The value of f(2) to f(n-2) will be calculated in two times. That will waste time. So, we can store the value of f(2) to f(n-1)

``` python
class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        l1 = 1
        l2 = 1
        l = 2
        for i in range(n-1):
            l = l1 + l2
            l1 = l2
            l2 = l
        return l
```
