#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        lastId = ""
        step = (numRows - 1) * 2
        length = len(s)
        res = ""
        for i in range(numRows):
            for j in range(length):
                leftId = i + step*j
                if (leftId < length):
                    if (lastId != leftId):
                        res += s[leftId]
                        lastId = leftId
                else:
                    break

                rightId = step * j + step - i
                if (rightId < length):
                    if (lastId != rightId):
                        res += s[rightId]
                        lastId = rightId
                else:
                    break
            #  print(res)
            #  print("++++++++++++++++++++")
        return res

solution = Solution()
#  print(solution.convert("PAYPALISHIRING", 3))
#  print(solution.convert("PAYPALISHIRING", 2))
print(solution.convert("AB", 1))
