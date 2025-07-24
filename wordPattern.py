class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False

        mapping = {}
        n = len(pattern)
        visited = set()
        for i in range(n):
            if pattern[i] not in mapping:
                if s_list[i] not in visited:
                    mapping[pattern[i]] = s_list[i]
                    visited.add(s_list[i])
                else:
                    return False
            else:
                if mapping[pattern[i]] != s_list[i]:
                    return False

        return True
