import heapq


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    contests.sort(key=lambda l: l[1], reverse=True)
    important = []
    heapq.heapify(important)
    unimportant = []
    S = 0
    for contest in contests:
        if contest[1] == 1:
            heapq.heappush(important, contest[0])
        else:
            unimportant.append(contest[0])

    S += sum(unimportant)
    n = len(important)
    for _ in range(n - k):
        if important:
            S -= heapq.heappop(important)
    for _ in range(k):
        if important:
            S += heapq.heappop(important)
    return S