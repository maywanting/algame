Add Binary
---

# Description

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

- Each string consists only of '0' or '1' characters.
- 1 <= a.length, b.length <= 10^4
- string is either "0" or doesn't contain any leading zero.

# Solution

There are two solutions for this question. Here is the simplest idea.

``` python
class Solution(object):
    def sumBin(self, a, b, c):
        sum = 0
        if a == '1':
            sum += 1
        if b == '1':
            sum += 1
        if c == '1':
            sum += 1

        if sum == 0:
            return ('0', '0')
        elif sum == 1:
            return ('0', '1')
        elif sum == 2:
            return ('1', '0')
        else:
            return ('1', '1')

    def addBinary(self, a, b):
        # print("==========")
        # print(a)
        # print(b)
        # print("---------------")
        len1 = len(a)
        len2 = len(b)
        basicItem = a
        addItem = b
        lenBasic = len1
        lenAdd = len2
        if len1 < len2:
            basicItem = b
            addItem = a
            lenBasic = len2
            lenAdd = len1
        res = ''

        pre = '0'
        for i in range(lenBasic):
            curBasic = basicItem[-1-i]
            curAdd = '0'
            if (-1-i + lenAdd) > -1:
                curAdd = addItem[-1-i]
            pre, cur = self.sumBin(curBasic, curAdd, pre)
            res = cur + res
            print(res)
        if pre == '1':
            res = pre + res
        return res
```

There is a nice idea using recursive solution.

``` python
class Solution(object):
    def addBinaryOther(self, a, b):
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinaryOther(self.addBinaryOther(a[0:-1], b[0, -1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinaryOther(a[0:-1], b[0, -1]) + '0'
        else:
            return self.addBinaryOther(a[0:-1], b[0, -1]) + '1'
```
