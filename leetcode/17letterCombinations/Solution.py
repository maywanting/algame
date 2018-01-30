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



solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
