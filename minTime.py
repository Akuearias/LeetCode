def minTime(machines, goal):
    machines.sort()
    L = 1
    R = machines[0] * goal
    while L < R:
        mid = (L + R) // 2
        S = sum(mid // m for m in machines)
        if S < goal:
            L = mid + 1
        else:
            R = mid
    return L