class Solution(object):
    def getPermutation(self, n, k):
        flag = 1
        for i in range(1, n+1):
            flag *= i
        listN = [str(i) for i in range(1, n+1)]
        k -= 1
        res = ''
        for i in range(n, 0, -1):
            # print("========")
            flag /= i
            index = k / flag
            k = k % flag
            res += listN[index]
            # print(listN[index])
            # print(index)
            listN = listN[:index] + listN[index+1:]
            # print(listN)
        return res
solution = Solution()
print(solution.getPermutation(4, 1))
print(solution.getPermutation(4, 9))
print(solution.getPermutation(3, 3))
