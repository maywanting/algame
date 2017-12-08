ZigZag Conversion
---

# Description

The string `PAYPALISHIRING` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `PAHNAPLSIIGYIR`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string text, int nRows);
```

`convert("PAYPALISHIRING", 3)` should return `PAHNAPLSIIGYIR`.

# Solution

The most important thing of this question is to know what is `ZigZag String`. Actually, I really don't understand what is `ZigZag String` until finding the explanation in the discusison.

When read `ZigZag String` line by line, I find a step on it. It means the order of line-by-line-string character is displayed a step in the `ZigZag String`.

You may say that the number of first line is different from the second when the numRows is larger than 2. I think the number of all the line is same, but, for example, in the first line, the `rightId` in step1 is same as the `leftId` in step2. So, they are merged.

This problem I used by python.

``` python

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
    return res
```

By the way, this problem can not handle the string when the numRows is 1. So...you know.
