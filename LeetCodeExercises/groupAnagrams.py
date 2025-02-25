import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        all_anagrams = {}
        for s in strs:
            if tuple(sorted(collections.Counter(s).items())) not in all_anagrams.keys():
                all_anagrams[tuple(sorted(collections.Counter(s).items()))] = [s]
            else:
                all_anagrams[tuple(sorted(collections.Counter(s).items()))].append(s)

        return list(all_anagrams.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))