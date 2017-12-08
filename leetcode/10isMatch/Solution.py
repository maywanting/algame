#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def changeP(self, p):
        res = []
        j = 0
        for i in range(len(p)):
            if p[i] == '*':
                res[j-1][1] = 1
            else :
                res.append([p[i], 0])
                j += 1
        return res

    def isMatch(self, s, p):
        pArray = self.changeP(p)
        flag = [[False for col in range(len(s) + 1)] for row in range(len(pArray) + 1)]
        flag[0][0] = True
        for i in range(len(pArray)):
            flag[i+1][0] = (pArray[i][1] is 1) and (flag[i][0] is 1)
            for j in range(len(s)) :
                if (s[j] is pArray[i][0]) or (pArray[i][0] == '.') : # match
                    if flag[i+1][0] : # *type
                        flag[i+1][j+1] = flag[i+1][j] or flag[i][j+1] or flag[i][j]
                    else: # simple type
                        print("i: " + str(i) )
                        for k in range(i) :
                            if flag[i - k][j] :
                                flag[i + 1][j + 1] = True
                                print("%d %d" % (i, k))
                                print(flag)
                                die()
                                break
                            if pArray[i - k][1] is 0:
                                print("%d %d" % (i, k))
                                print(flag)
                                die()
                                break
            print(flag)
        return flag[len(pArray)][len(s)]


solution = Solution()
#  print(solution.isMatch("aa", "a")) #false
#  print(solution.isMatch("aa", "aa")) #true
#  print(solution.isMatch("aaa", "aa")) #false
#  print(solution.isMatch("aa", "a*")) #true
#  print(solution.isMatch("aa", ".*")) #true
#  print(solution.isMatch("ab", ".*")) #true
#  print(solution.isMatch("aab", "c*a*b")) #true
#  print(solution.isMatch("a", "")) #false
#  print(solution.isMatch("ab", ".*c")) #false
#  print(solution.isMatch("aaa", "aaaa")) #false
#  print(solution.isMatch("aaa", "a*a")) #true
print(solution.isMatch("aaa", "ab*ac*a")) #true
#  solution.isMatch("aab", "c*a*b") #false
