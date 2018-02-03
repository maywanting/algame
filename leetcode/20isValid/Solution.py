class Solution(object):
    bracketsMap = {
        '(': 1,
        ')': -1,
        '[': 2,
        ']': -2,
        '{': 3,
        '}': -3,
    }

    def isValid(self, s):
        justifyArray = []
        for i in range(len(s)):
            length = len(justifyArray)
            currentValue = self.bracketsMap[s[i]]
            if length > 0:
                if (justifyArray[length - 1] + currentValue) == 0:
                    justifyArray.pop()
                else:
                    justifyArray.append(currentValue)
            else:
                justifyArray.append(currentValue)
        #  print(justifyArray)
        return len(justifyArray) == 0



solution = Solution()
print(solution.isValid("[")) #false
print(solution.isValid('()[{}]()'))
