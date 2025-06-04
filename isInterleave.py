class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == len(s2) == len(s3) == 0:
            return True
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        inters = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        inters[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                dummy = i + j - 1
                if i > 0:
                    inters[i][j] |= (inters[i - 1][j] & (s1[i - 1] == s3[dummy]))
                if j > 0:
                    inters[i][j] |= (inters[i][j - 1] & (s2[j - 1] == s3[dummy]))

        return inters[-1][-1]
