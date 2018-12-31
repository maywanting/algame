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

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
