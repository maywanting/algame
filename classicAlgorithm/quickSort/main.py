def quickSortLoop(arr, start, end):
    flag = arr[end]
    originStart, originEnd = start, end
    if (originEnd - originStart) < 1:
        return

    while (start < end):
        while (arr[start] < flag) and start < end:
            start += 1
        arr[end] = arr[start]
        while (arr[end] > flag) and start < end:
            end -= 1
        arr[start] = arr[end]
    arr[start] = flag

    quickSortLoop(arr, originStart, start-1)
    quickSortLoop(arr, start+1, originEnd)

def quickSort(arr):
    quickSortLoop(arr, 0, len(arr)-1)

arr = [3, 56, 2, 54, 99, 34, 83, 57]
quickSort(arr)
print(arr)
