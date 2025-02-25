import collections
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = dict(collections.Counter(chars))
        counter_keys = list(counter.keys())
        counter_values = list(counter.values())
        for i in range(len(counter_values)):
            if counter_values[i] >= 10:
                val = counter_values[i]
                counter_values[i] = str(val)

        compress_list = []
        for i in range(len(counter_values)):
            if n =





