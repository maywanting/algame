#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def updatePattern(self, p, j) :
        if (j + 1) < len(p) and (p[j+1] == '*'):
            return j + 2, 0, p[j]
        else :
            return j + 1, 1, p[j]

    def canPattern(self, p, j) :
        return j < len(p)

    def canString(self, s, i) :
        return i < len(s)

    def updateString(self, s, i) :
        return i+1, s[i]

    def isMatch(self, s, p):
        i, j = 0, 0
        if self.canPattern(p, j):
            j, length, mChar = self.updatePattern(p, j)
            print("%c %d" % (mChar, length))
        else:
            return False

        if self.canString(s, i):
            i, checkChar = self.updateString(s, i)
            print("%c %c" % (checkChar, mChar))
        else:
            return False

        while True:
            if checkChar != mChar and mChar != '.' :
                if length == 0 : # updatePattern
                    if self.canPattern(p, j) :
                        j, length, mChar = self.updatePattern(p, j)
                        print("ptype1: %c %c %d" % (checkChar, mChar, length))
                        continue
                    else :
                        print("11111111")
                        return not self.canString(s, i)
                else:
                    print("2222222")
                    return False

            if self.canString(s, i):
                i, checkChar = self.updateString(s, i)
                print("stype: %c %c" % (checkChar, mChar))
                if length != 0:
                    if self.canPattern(p, j):
                        j, length, mChar = self.updatePattern(p, j)
                        print("ptype2: %c %c %d" % (checkChar, mChar, length))
                    else:
                        print("333333333")
                        return not self.canString(s, i-1)
            else :
                print("44444444")
                return not self.canPattern(p, j)


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
print(solution.isMatch("aaa", "a*a")) #false
