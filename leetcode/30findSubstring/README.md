Substring with Concatenation of All Words
---

# Description

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: `"barfoothefoobarman"`
words: `["foo", "bar"]`

You should return the indices: [0,9].
(order does not matter).

# Solution

First time I think the elements in words is unrepeated. But the fact is it can be repeated. So, one dictionary is used to store the elements and the occurances number in words.

``` python
class Solution(object):
    def findSubstring(self, s, words):
        length, res, wordsLen, wordsDics = len(words[0]), [], len(words), {}
        for i in range(length):
            string = s[i:]
            matchMap, times = [], 0
            while len(string) >= length:
                now = string[:length]
                times += 1

                # store the occurance number
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
                else: #shut down, clean the matchMap
                    matchMap= []
                string = string[length:]
        return res
```
