class Solution(object):
    def trap(self, height):
        #find pole
        pole = []
        length = len(height)
        if (length < 3):
            return 0
        for current in range(1, length-1):
            if (height[current - 1] <= height[current]) and (height[current] >= height[current + 1]):
                pole += [[current, height[current]]]

        #judge head
        if (height[0] > height[1]):
            pole = [[0, height[0]]] + pole

        #judge tail
        if (height[length-1] > height[length-2]):
            pole += [[length-1, height[length-1]]]

        lastPole = []
        while (len(pole) > 1) and (len(lastPole) != len(pole)):
            print(pole)
            lastPole = pole
            pole = [lastPole[0]]
            length = len(lastPole)
            if (length < 3):
                continue
            for current in range(1, length-1):
                if (lastPole[current - 1][1] >= lastPole[current][1]) and (lastPole[current][1] <= lastPole[current + 1][1]):
                    continue
                pole += [lastPole[current]]
            pole += [lastPole[length-1]]

        print(lastPole)
        last = []
        allRes = 0
        for row in lastPole:
            if len(last) == 0:
                last = row
            else:
                hei = min(last[1], row[1])
                for i in range(last[0]+1, row[0]):
                    res = hei - height[i]
                    # print(res)
                    allRes += max(res, 0)
                last = row
        return allRes

solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) #6
print(solution.trap([5, 4, 1, 2])) #1
print(solution.trap([5, 2, 1, 2, 1, 5])) #14
print(solution.trap([4, 2, 0, 3, 2, 4, 3, 4])) #10
print(solution.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])) #23
print(solution.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) #83
