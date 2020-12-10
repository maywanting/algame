class Solution(object):
    def simplifyPath(self, path):
        pathList = path.split('/')
        resList = []

        for item in pathList:
            if (item == '..'):
                if len(resList) > 0:
                    resList.pop()
            elif (item != '') and (item != '.'):
                resList.append(item)

        return '/' + '/'.join(resList)
solution = Solution()
print(solution.simplifyPath('/home/'))
print(solution.simplifyPath('/../'))
print(solution.simplifyPath('/home//foo/'))
print(solution.simplifyPath('/a/./b/../../c/'))
