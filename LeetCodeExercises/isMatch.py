class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 ^ len(p) == 0:
            return False

        
