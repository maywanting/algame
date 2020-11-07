Text Justification
---

# Description

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

- A word is defined as a character sequence consisting of non-space characters only.
- word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- input array words contains at least one word.

Example 1:
```
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```
Example 2:
```
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
```
Example 3:
```
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```
# Solution

I think the main point we should regard is when the number of word in a line being one. And other things are simple.

``` python
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
```
