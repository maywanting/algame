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

solution = Solution()
# print(solution.multiply('2', '3')) #6
print(solution.multiply('123', '456')) #56088
print(solution.multiply('0', '9133'))
