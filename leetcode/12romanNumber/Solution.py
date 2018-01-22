class Solution(object):
    def intToRoman(self, num):
        charMap = {
            'M': ['', 'M', 'MM', 'MMM'],
            'C': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            'X': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            'I': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        }

        return charMap['M'][num / 1000] + charMap['C'][(num / 100) % 10] + charMap['X'][(num / 10) % 10] + charMap['I'][num % 10]

solution = Solution()
print(solution.intToRoman(1))
print(solution.intToRoman(2))
print(solution.intToRoman(4))
print(solution.intToRoman(5))
print(solution.intToRoman(6))
print(solution.intToRoman(9))
print(solution.intToRoman(134))
