# -*- coding: utf-8 -*-

dic = []
maps = ['a', 'b', 'c', 'd']
origin = 7
length = -1
node = -1
for i in range(7):
    if len(dic)
def loop (pre, num):
    if num < origin:
        i = num
        while i > 0:
            print(pre + maps[i-1])
            i -= 1
    else:
        loop(pre + maps[0], num / 4)
        loop(pre + maps[1], num / 4)
        loop(pre + maps[2], num / 4)
        loop(pre + maps[3], num / 4)

loop('', origin)
