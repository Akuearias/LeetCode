def riddle(arr):
    n = len(arr)
    res = [0] * (n + 1)
    stack = []

    left = [-1] * n
    right = [n] * n

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    for i in range(n):
        length = right[i] - left[i] - 1
        res[length] = max(res[length], arr[i])

    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])

    return res[1:]