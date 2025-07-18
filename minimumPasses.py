def minimumPasses(m, w, p, n):
    import math

    min_passes = math.inf
    candies = 0
    passes = 0

    while candies < n:
        # Calculate the rounds can reach without purchases
        min_passes = min(min_passes, passes + math.ceil((n - candies) / (m * w)))

        # If not enough money, skip until being able to purchase
        if candies < p:
            extra_passes = math.ceil((p - candies) / (m * w))
            passes += extra_passes
            candies += extra_passes * m * w
            continue

        # If enough money, purchase workers/machines as many as possible
        total_units = candies // p
        candies -= total_units * p

        # Distribute the new-purchased units into m and w and try to balance them (maximize the production amount)
        total = m + w + total_units
        half = total // 2
        if m > w:
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w

        # Simulation
        candies += m * w
        passes += 1

    return min(passes, min_passes)