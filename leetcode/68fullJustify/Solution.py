class Solution(object):
    def fullJustify(self, words, maxWidth):

        n = 0 #the length of temList
        temList = []
        l = 0 #the length of characters in temList
        res = []

        for word in words:
            lenWord = len(word)
            if (l + lenWord + n) <= maxWidth:
                temList.append(word)
                n += 1
                l += lenWord
            else:
                space = maxWidth - l
                if n == 1:
                    perS = space
                    leftS = 0
                else:
                    perS = space / (n - 1)
                    leftS = space % (n-1)

                perSpace = ' ' * perS
                resStr = ''

                if n == 1:
                    resStr = temList[0] + perSpace
                else:
                    if leftS > 0:
                        resStr = (perSpace + ' ').join(temList[0:leftS])
                        resStr += perSpace + ' '
                    resStr += perSpace.join(temList[leftS:])
                res.append(resStr)
                temList = [word]
                n = 1
                l = lenWord

        #last line
        resStr = ' '.join(temList)
        spaceNum = maxWidth - l - n + 1
        resStr += ' ' * spaceNum
        res.append(resStr)

        return res


solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
print(solution.fullJustify(["Listen","to","many,","speak","to","a","few."], 6))
