class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i1, i2 = int(a, base=2), int(b, base=2)
        S = bin(i1 + i2)
        return S[2:]
