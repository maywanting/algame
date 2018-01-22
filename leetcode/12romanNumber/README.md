Integer to Roman
---

# Description

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

# Solution

By the chance, I learn about what is raman number.

I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

The algorithm is very easy... really easy

``` python
class Solution(object):
    def intToRoman(self, num):
        charMap = {
            'M': ['', 'M', 'MM', 'MMM'],
            'C': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            'X': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            'I': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        }

        return charMap['M'][num / 1000] + charMap['C'][(num / 100) % 10] + charMap['X'][(num / 10) % 10] + charMap['I'][num % 10]
```
