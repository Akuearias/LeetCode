def substrCount(n, s):
    groups = []
    prev = ''
    count = 0
    for c in s:
        if c == prev:
            count += 1
        else:
            if prev:
                groups.append((prev, count))
            prev = c
            count = 1
    groups.append((prev, count))

    S = 0

    for ch, cnt in groups:
        S += cnt * (cnt + 1) // 2

    for i in range(1, len(groups) - 1):
        if groups[i][1] == 1 and groups[i - 1][0] == groups[i + 1][0]:
            S += min(groups[i - 1][1], groups[i + 1][1])

    return S