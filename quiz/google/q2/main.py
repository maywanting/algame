with open('./task2-test-input.txt') as f:
    number = int(f.readline())
    maps = {}
    for i in range(number):
        flag = f.readline()
        lineNum = int(f.readline())
        for line in range(lineNum-1):
            meg = f.readline().split()
            print(meg)
            node1 = int(meg[0])
            node2 = int(meg[1])
            if node1 in maps:
                maps[node1] += [node2]
            else:
                maps[node1] = [node2]
        print(maps)
