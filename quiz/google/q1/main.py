def getClose(price1, price2, price):
    res1 = abs(price1-price)
    res2 = abs(price2-price)
    if res1 ==  res2:
        return min(price1, price2)
    elif res1 > res2:
        return price2
    else:
        return price1

res = []
with open('./task1-test-input.txt') as f:
    number = int(f.readline())
    for i in range(number):
        flag = f.readline()
        price = int(f.readline())
        flavorNum = int(f.readline())
        flavor = []
        print(price)
        for fn in range(flavorNum):
            line = f.readline().split()
            flavor += [int(line[1])]

        flavor.sort()
        # flavor = sorted(flavor.items(), key=lambda x:x[1])
        print(flavor)
        optionNum = int(f.readline())
        option = []
        for on in range(optionNum):
            line = f.readline().split()
            option += [int(line[1])]
        option.sort()

        close = flavor[0]
        for fla in flavor:
            tmpClose = fla
            for opt in option:
                tmpClose = getClose(opt + fla, tmpClose, price)
            close = getClose(tmpClose, close, price)
            if len(option) < 2:
                continue
            for j in range(len(option)-1):
                for k in range(j, len(option)):
                    tmpClose = getClose(fla + option[j] + option[k], tmpClose, price)

            close = getClose(tmpClose, close, price)

        res += ["Case #%d: %d" % (i+1, close)]
        print(close)

        print("========")

with open('./task1-test-output.txt', mode='w') as o:
    o.write('\n'.join(res))
