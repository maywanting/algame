#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def changeP(self, p):
        res = [['$', 0]] # start mark
        j = 1
        for i in range(len(p)):
            if p[i] == '*':
                res[j-1][1] = 1
            else :
                res.append([p[i], 0])
                j += 1
        return res

    def isMatch(self, s, p):
        pArray = self.changeP(p)
        s = '$' + s
        flag = [[False for col in range(len(s))] for row in range(len(pArray))]
        flag[0][0] = True
        for i in range(1, len(pArray)):
            for j in range(len(s)):
                if (s[j] is pArray[i][0]) or (pArray[i][0] == '.' and s[j] != '$'): # match
                    if pArray[i][1] : # *type
                        flag[i][j] = flag[i-1][j-1] or flag[i-1][j] or flag[i][j-1]
                    else: # simple type
                        flag[i][j] = flag[i-1][j-1]
                else: # not match
                    if pArray[i][1]:  #*type
                        flag[i][j] = flag[i-1][j]
        print(flag)
        return flag[len(pArray)-1][len(s)-1]

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
#  print(solution.isMatch("aaa", "ab*ac*a")) #true
#  print(solution.isMatch("aa", "aa*a")) #true
#  print(solution.isMatch("aab", "c*a*b")) #true
#  print(solution.isMatch("aab", "c*b")) #true
print(solution.isMatch("a", ".*..a*")) #false
