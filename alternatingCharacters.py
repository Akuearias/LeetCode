def alternatingCharacters(s):
    stack = []
    S = 0
    for i in range(len(s)):
        if not stack or stack[-1] != s[i]:
            stack.append(s[i])
        else:
            S += 1
    return S