def superDigit(n, k):
    p = sum(int(char) for char in n)
    return superDigitHelper(str(p * k))

def superDigitHelper(p):
    if len(p) == 1:
        return int(p)
    else:
        S = 0
        for char in p:
            S += int(char)
        return superDigitHelper(str(S))