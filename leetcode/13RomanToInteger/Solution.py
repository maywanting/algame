class Solution(object):
    def romanToInt(self, s):
        romanMap = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and romanMap[s[i]] < romanMap[s[i+1]]: #minus
                res -= romanMap[s[i]]
            else: #plus
                res += romanMap[s[i]]

        return res


solution = Solution()

#  print(solution.romanToInt('CXXXIV')) #134
print(solution.romanToInt('DCXXI')) #621
