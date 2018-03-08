class Solution(object):
    def findSubstring(self, s, words):
        length, res, wordsLen, wordsDics = len(words[0]), [], len(words), {}
        for i in range(length):
            string = s[i:]
            print(string)
            matchMap, times = [], 0
            while len(string) >= length:
                now = string[:length]
                times += 1
                print(now)
                if not wordsDics.has_key(now):
                    wordsDics[now] = words.count(now)
                wordsNumber = wordsDics[now]
                if wordsNumber > 0: #get the index
                    time = words.index(now)
                    if matchMap.count(time) >= wordsNumber:
                        flag = matchMap.index(time)
                        matchMap = matchMap[flag+1:]

                    matchMap.append(time)
                    if len(matchMap) == wordsLen:
                        res.append(i + times*length - length*wordsLen)
                        print("FIND")
                        print(res)
                        print("=========")
                else: #shut down, clean the matchMap
                    matchMap= []
                string = string[length:]
                print(matchMap)

        return res

solution = Solution()
#  print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"])) #[0, 9]
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])) #[8]
