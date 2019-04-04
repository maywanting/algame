import sys

num = int(raw_input())
alpha = ['A', 'B', 'C', 'D']
n = num

if n < 4:
    for i in range(n):
        print(alpha[i])
    sys.exit()

count = 0
base = 1

while n > 1:
    n /= 4.0
    count += 1
    base *= 4

base /= 4
if base == 1:
    base = 0

gap = num - base

def dfs(p, now):
    if p == count - 1:
        global gap
        if gap > 0:
            gap += 1
            for i in range(4):
                print(now + alpha[i])
                gap -= 1
                if gap == 0:
                    break
                else:
                    print(now)
    else:
        for i in range(4):
            dfs(p + 1, now + alpha[i])

dfs(0, '')



