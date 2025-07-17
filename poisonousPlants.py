def poisonousPlants(p):
    stack = []
    S = 0

    for plant in p:
        d = 0

        while stack and plant <= stack[-1][0]:
            d = max(d, stack[-1][1])
            stack.pop()

        if not stack:
            d = 0
        else:
            d += 1

        S = max(S, d)
        stack.append((plant, d))

    return S