Minimum Window Substring
---

# Description

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

# Solution

The most import point is to create a hash table to store the character frequency in 't'. Also, we need to figure out the number of characters.


``` python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {} # hash table of the characters frequency in t
        ms, me = 0, 0
        lenNeed = len(t) # the number of character in 't' we still need.

        if lenNeed > len(s): return ""

        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        
        i = 0
        for j, c in enumerate(s, 1):
            if c in t:
                if need[c] > 0: #if the frequency of character in window is bigger than that in 't', lenNeed will not decrease
                    lenNeed -= 1  
                need[c] -= 1
            
            if lenNeed == 0:
                while (i < j) and (s[i] not in t or need[s[i]] < 0):
                    if s[i] in need:
                        need[s[i]] += 1
                    i += 1
                
                if me == 0 or (j-i < me - ms):
                    ms, me = i, j
                
                need[s[i]] += 1
                i += 1
                lenNeed += 1
        
        return s[ms:me]
```