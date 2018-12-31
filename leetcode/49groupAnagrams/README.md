Group Anagrams
---

# Description

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

- All inputs will be in lowercase.
- order of your output does not matter.

# Solution

The process of solution is to sort the order of character and then group them by SET structure.

``` python
class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for item in strs:
            temp = list(item)
            temp.sort()
            sortRes = ''.join(temp)
            if sortRes in res:
                res[sortRes] += [item]
            else:
                res[sortRes] = [item]
        return res.values()
```
