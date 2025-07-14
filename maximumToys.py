def maximumToys(prices, k):
    prices.sort(reverse=True)
    S = 0
    while prices:
        if prices[-1] <= k:
            k -= prices.pop()
            S += 1
        else:
            break
    return S