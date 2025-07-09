def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(m):
        for j in range(n + 1):
            if dp[i][j]:

                if a[i].islower():
                    dp[i + 1][j] = True

                if j < n and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True

    return 'YES' if dp[m][n] else 'NO'