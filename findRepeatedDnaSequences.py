class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        if n <= 10:
            return []

        seqs = set()
        visited = set()

        for i in range(n - 9):
            dummy = s[i:i+10]
            if dummy in visited:
                seqs.add(dummy)
            visited.add(dummy)

        return list(seqs)
