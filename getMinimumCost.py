def getMinimumCost(k, c):
    c.sort(reverse=True)
    S = 0
    for i in range(len(c)):
        S += (i // k + 1) * c[i]

    return S

