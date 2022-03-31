class Solution(object):
    def minWindow(self, s, t):
        need = {} # hash table of the characters frequency in t
        ms, me = 0, 0
        lenNeed = len(t)

        if lenNeed > len(s): return ""

        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1

        i = 0
        for j, c in enumerate(s, 1):
            if c in t:
                if need[c] > 0:
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



solution = Solution()
# print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("ADOBECODABANC", "ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("a", "aa"))
