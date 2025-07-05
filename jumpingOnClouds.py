#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    i = 0
    S = 0
    while i < len(c) - 1:
        if i + 2 < len(c):
            if c[i + 2] == 0:
                i += 2
            else:
                i += 1
        else:
            i += 1
        S += 1

    return S