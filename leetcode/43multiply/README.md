Multiply Strings
---

# Description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

Example 2:

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Solution

Most important thing in this question is understand the algorithm of multiply. I think the main algorithm of multiply has been taught in primary school.

I still remember the algorithm beacuse it have been used so much times until I go to the university.

So the solution of this problem is using the human-being calculation algorithm. Also, pay attention to the get the ASCII code of character.

``` python
class Solution(object):
    def multiply(self, num1, num2):
        len1, len2 = len(num1), len(num2)
        res = [0 for i in range(len1 + len2)]

        for i in range(len1):
            numi = ord(num1[len1-1-i]) - ord('0')
            for j in range(len2):
                numj = ord(num2[len2-1-j]) - ord('0')
                mul = numi*numj
                res[len1+len2-1-i-j] += mul
                res[len1+len2-2-i-j] += res[len1+len2-1-i-j] / 10
                res[len1+len2-1-i-j] %= 10

        for flag, i in enumerate(res):
            if i > 0:
                break

        resStr = [chr(i + ord('0')) for i in res]
        return ''.join(resStr[flag:])
```
