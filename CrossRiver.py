def maxTrailing(arr):
    n = len(arr)
    maxDiff = float('-inf')
    minElem = float('inf')

    for i in range(n):
        if arr[i] > minElem:
            maxDiff = max(maxDiff, arr[i] - minElem)
        else:
            minElem = arr[i]

    return maxDiff if maxDiff != float('-inf') else -1

arr = [7, 2, 3, 10, 2, 4, 8, 1]
result = maxTrailing(arr)
print(result)
