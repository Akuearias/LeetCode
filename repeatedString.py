#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    initial_count = 0
    for c in s:
        if c == 'a':
            initial_count += 1

    S = 0
    S += n // len(s) * initial_count
    remain = n % len(s)
    if remain != 0:
        for c in s[:remain]:
            if c == 'a':
                S += 1
    return S