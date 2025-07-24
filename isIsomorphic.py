class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        n = len(s)
        visited = set()
        for i in range(n):
            if s[i] not in mapping:
                if t[i] not in visited:
                    mapping[s[i]] = t[i]
                    visited.add(t[i])
                else:
                    return False
            else:
                if mapping[s[i]] != t[i]:
                    return False

        return True