#!/usr/bin/env python
# encoding: utf-8

timemap = [
    [0, 3, 'A1'], #A1
    [3, 5, 'A2'], #A2
    [5, 2, 'A3'], #A3
    [2, 3, 'A4'], #A4
    [3, 4, 'A5'], #A5
    [4, 3, 'A6'], #A6
    [3, 4, 'A7'], #A7
    [4, 2, 'A8'], #A8
    [2, 2, 'A9'], #A9
    [2, 3, 'A10'], #A10
    [3, 6, 'A11'], #A11
    [6, 2, 'A12'], #A12
    [2, 0, 'A13'], #A13
    [0, 4, 'B1'], #B1
    [4, 3, 'B2'], #B2
    [3, 3, 'B3'], #B3
    [3, 2, 'B4'], #B4
    [2, 3, 'B5'], #B5
    [3, 1, 'B6'], #B6
]

def getPlusTime(end, nextMinu):
    endTime = end.split(':')
    if (int(endTime[1]) + nextMinu >= 60):
        return "{:0>2d}:{:0>2d}".format(int(endTime[0]) + 1, (int(endTime[1]) + nextMinu) % 60)
    else :
        # return endTime[0] + ':' + str(int(endTime[1]) + nextMinu)
        return "{:0>2d}:{:0>2d}".format(int(endTime[0]), int(endTime[1]) + nextMinu)

def getTime(start, end, timeStep, run):
    start = getPlusTime(start, run)
    startTime = start.split(':')
    endTime = end.split(':')
    minu = (int(endTime[0]) - int(startTime[0])) * 60 + (int(endTime[1]) - int(startTime[1]))
    nextMinu = timeStep - (minu % timeStep)

    if (int(endTime[1]) + nextMinu >= 60):
        return "{:0>2d}:{:0>2d}".format(int(endTime[0]) + 1, (int(endTime[1]) + nextMinu) % 60)
    else :
        # return endTime[0] + ':' + str(int(endTime[1]) + nextMinu)
        return "{:0>2d}:{:0>2d}".format(int(endTime[0]), int(endTime[1]) + nextMinu)

def singleRoute(start, end, time):
    # print(start)
    # print(end)
    trainTime = 0
    trainRunTime = 0
    trainStartTime = time
    endTime = time
    if start < end: # timemap1
        for i in range(start, end):
            trainTime += timemap[i][1]
        if (7 > end): #lineA A1->A7
            for i in range(start):
                trainRunTime += timemap[i][1]
            trainStartTime = getTime('05:55', time, 5, trainRunTime)
            endTime = getPlusTime(trainStartTime, trainTime)
        elif (end <= 12): #lineA A1->A13
            for i in range(start):
                trainRunTime += timemap[i][1]
            trainStartTime = getTime('06:00', time, 10, trainRunTime)
            endTime = getPlusTime(trainStartTime, trainTime)
        else: #lineB B1->B6
            for i in range(13, start):
                trainRunTime += timemap[i][1]
            trainStartTime = getTime('06:00', time, 6, trainRunTime)
            endTime = getPlusTime(trainStartTime, trainTime)

    else: # timemap0
        for i in range(start, end-1, -1):
            trainTime += timemap[i][0]
        if (13 > end): #lineA A13->A1
            for i in range(start, end-1, -1):
                trainRunTime += timemap[i][0]
            trainStartTime = getTime('05:55', time, 5, trainRunTime)
            endTime = getPlusTime(trainStartTime, trainTime)
        elif(end > 12): #lineB B6->B1
            for i in range(17, start, -1):
                trainRunTime += timemap[i][0]
            trainStartTime = getTime('06:11', time, 6, trainRunTime)
            endTime = getPlusTime(trainStartTime, trainTime)
    return [trainStartTime, endTime]

def main(argv):
    #index A, number-1, B, number+12
    start = argv[0]
    end = argv[1]
    time = argv[2]
    if start[0] == end[0]: # same line
        if start[0] == 'A':
            rest = singleRoute(int(start[1])-1, int(end[1:])-1, time)
            print(start[0] + ' ' + start + ' ' + rest[0] + ' - ' + end + ' ' + rest[1])
        if start[0] == 'B':
            rest = singleRoute(int(start[1])+12, int(end[1:])+12, time)
            print(start[0] + ' ' + start + ' ' + rest[0] + ' - ' + end + ' ' + rest[1])
    else:
        if start[0] == 'A':
            rest1 = singleRoute(int(start[1])-1, 6, time)
            print(start[0] + ' ' + start + ' ' + rest1[0] + ' - ' + 'A7' + ' ' + rest1[1])
            rest2 = singleRoute(17, int(end[1:]) + 12, getPlusTime(rest1[1], 1))
            print(end[0] + ' ' + 'A7' + ' ' + rest2[0] + ' - ' + end + ' ' + rest1[1])

# main(['A3', 'A11', '22:26'])
main(['A1', 'B3', '08:26'])
# main(['A6', 'A7', '21:12'])
