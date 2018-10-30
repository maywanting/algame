class Solution(object):
    def countAndSay(self, n):
        res = '1'
        n -= 1
        while (n):
            last = res
            res = ''
            while (len(last) != 0):
                char = last[0]
                num = 1
                while (num < len(last) and char == last[num]):
                    num += 1
                res += str(num) + char
                last = last[num:]
            n -= 1
            # print(res)
        return res

solution = Solution()
print(solution.countAndSay(5))
