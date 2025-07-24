import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1, dict2 = collections.Counter(ransomNote), collections.Counter(magazine)
        for char in dict1:
            if char not in dict2 or dict1[char] > dict2[char]:
                return False

        return True
