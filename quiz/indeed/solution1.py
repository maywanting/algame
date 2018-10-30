# n = int(raw_input())

# A = []
# for i in range(n):
    # A.append(int(raw_input()))

# S = raw_input()

n = 6
A = [190, 220, 783, 299, 212, 167]
S = "DWWLLW"
maxNum, minNum = 0, 0
for i in range(n):
    avg = A[i] / 2
    print(avg)
    odd = A[i] % 2
    if S[i] == 'D':
        maxNum += avg
        minNum += avg
    elif S[i] == 'W':
        maxNum += A[i]
        minNum += avg + 1
    else: #L
        if odd == 1:
            maxNum += avg
        else:
            maxNum += avg -1

print(str(minNum) + " " + str(maxNum))
