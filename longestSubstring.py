import collections
import re


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        char_freq = dict(collections.Counter(s))

        invalids = [c for c, c_count in char_freq.items() if c_count < k]

        if not invalids:
            return len(s)

        splits = f"[{''.join(invalids)}]"
        subs = re.split(splits, s)

        return max((self.longestSubstring(sub, k) for sub in subs if len(sub) >= k), default=0)
