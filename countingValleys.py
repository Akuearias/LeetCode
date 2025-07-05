#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    levels = [0]
    if path[0] == 'D':
        levels.append(-1)
    else:
        levels.append(1)
    for i in range(1, steps):
        if path[i] == 'D':
            levels.append(levels[-1] - 1)
        else:
            levels.append(levels[-1] + 1)

    S = 0
    L, R = 0, 1
    while L < steps:
        if levels[L] == 0:
            if levels[L + 1] < 0:
                S += 1
            while R <= steps and levels[R] != 0:
                R += 1
        L = R
        R += 1

    return S