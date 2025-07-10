import math


def primality(n):
    if n == 1:
        return 'Not prime'

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'Not prime'

    return 'Prime'