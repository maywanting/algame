Letter Combinations of a Phone Number
---

# Description

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## Note

Although the above answer is in lexicographical order, your answer could be in any order you want.

# Solution

This problem is a DP(Dynamic programming) problem. So the problem will be divided with three type

- when the length of digits is 0

> return []

- when the length of digits id 1

> return the charachters array searching from map

- when the length of digits is larger than 1

> get the return array of digits without the first charachter, and than using the return array and the map array according to the first character, get the new result array of the combinations with this two arrays

``` python
class Solution(object):
    digitMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        if len(digits) <= 1:
            if len(digits) == 0:
                return []
            else:
                return self.digitMap[digits[0]]

        current = self.digitMap[digits[0]]
        other = self.letterCombinations(digits[1:])

        res = []
        for i in range(len(current)):
            for j in range(len(other)):
                res.append(current[i] + other[j])

        return res
```
