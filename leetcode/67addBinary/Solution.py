class Solution(object):
    def sumBin(self, a, b, c):
        sum = 0
        if a == '1':
            sum += 1
        if b == '1':
            sum += 1
        if c == '1':
            sum += 1

        if sum == 0:
            return ('0', '0')
        elif sum == 1:
            return ('0', '1')
        elif sum == 2:
            return ('1', '0')
        else:
            return ('1', '1')

    def addBinary(self, a, b):
        # print("==========")
        # print(a)
        # print(b)
        # print("---------------")
        len1 = len(a)
        len2 = len(b)
        basicItem = a
        addItem = b
        lenBasic = len1
        lenAdd = len2
        if len1 < len2:
            basicItem = b
            addItem = a
            lenBasic = len2
            lenAdd = len1
        res = ''

        pre = '0'
        for i in range(lenBasic):
            curBasic = basicItem[-1-i]
            curAdd = '0'
            if (-1-i + lenAdd) > -1:
                curAdd = addItem[-1-i]
            pre, cur = self.sumBin(curBasic, curAdd, pre)
            res = cur + res
            print(res)
        if pre == '1':
            res = pre + res
        return res

    def addBinaryOther(self, a, b):
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinaryOther(self.addBinaryOther(a[0:-1], b[0, -1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinaryOther(a[0:-1], b[0, -1]) + '0'
        else:
            return self.addBinaryOther(a[0:-1], b[0, -1]) + '1'

solution = Solution()
print(solution.addBinary("11", '1'))
print(solution.addBinary("1010", '1011'))
