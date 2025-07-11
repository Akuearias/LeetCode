def largestRectangle(h):
    h.append(-1)
    stack = []
    S = 0
    for i in range(len(h)):
        while stack and h[i] < h[stack[-1]]:
            H = h[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            S = max(S, H * W)
        stack.append(i)
    return S