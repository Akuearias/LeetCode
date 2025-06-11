class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a_stats = {chr(ord('a') + i): 0 for i in range(26)}
        b_stats = {chr(ord('a') + i): 0 for i in range(26)}

        m = len(a)
        n = len(b)

        for i in range(len(a)):
            a_stats[a[i]] += 1

        for j in range(len(b)):
            b_stats[b[j]] += 1

        S = math.inf
        Sa = 0
        Sb = 0
        for i in range(25):
            Sa += a_stats[chr(ord('a') + i)]
            Sb += b_stats[chr(ord('a') + i)]
            S = min(min(S, m - a_stats[chr(ord('a') + i)] + n - b_stats[chr(ord('a') + i)]),
                    min(m - Sa + Sb, n - Sb + Sa))
        S = min(S, m - a_stats['z'] + n - b_stats['z'])

        return S
