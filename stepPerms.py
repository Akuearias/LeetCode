def stepPerms(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    DP = [1, 2, 4] + [0] * (n - 3)
    for i in range(3, n):
        DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]
    return DP[-1] % (10 ** 10 + 7)