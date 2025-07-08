def minimumAbsoluteDifference(arr):
    arr.sort()
    diff = []
    for i in range(1, len(arr)):
        diff.append(abs(arr[i] - arr[i - 1]))

    diff.sort()
    return diff[0]