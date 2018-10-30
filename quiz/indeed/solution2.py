# n = int(raw_input())

# A = []
# for i in range(n):
    # A.append(int(raw_input()))

# S = raw_input()
# N, M, r, c = map(int, raw_input().split())
# S = raw_input()
N = 314159265
M = 398979323
r = 84626433
c = 83279502
S = "UDRLDRUD"

blackNmap = {} #heng
blackMmap = {} #zong

def updateMap(r, c):
    if (blackNmap.has_key(r)) :
        blackNmap[r].add(c)
    else:
        blackNmap[r] = set([c])
    if (blackMmap.has_key(c)) :
        blackMmap[c].add(r)
    else:
        blackMmap[c] = set([r])

lastr, lastc = r, c

for op in S:
    flag = 0
    if op == 'U':
        maxValue = 0
        for value in blackMmap[c]:
            if (value < r) and (value > maxValue) :
                maxValue = value

        # if r != (maxValue + 1)
        r = maxValue + 1
    elif op == 'D':
        minValue = N+1
        for value in blackMmap[c]:
            if (value > r) and (value < minValue):
                minValue = value
        r = minValue - 1
    elif op == 'L':
        maxValue = 0
        for value in blackNmap[r]:
            if (value < r) and (value > maxValue):
                maxValue = value
        c = maxValue + 1
    else: #R
        minValue = M + 1
        for value in blackNmap[r]:
            if (value > r) and (value < minValue):
                minValue = value
        c = minValue - 1
    if (lastr != r) or (lastc != c):
        updateMap(lastr, lastc)
        lastr, lastc = r, c
    print(str(r) + " " + str(c))
    # print(blackMmap)
    # print(blackNmap)
