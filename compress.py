import collections
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        newChar = ""
        k = 1
        while j <= len(chars) - 1:
            if chars[i] == chars[j]:
                if i != j:
                    k += 1
                else:
                    newChar += chars[i]
                j += 1
            else:
                if k > 1:
                    newChar += str(k)
                i = j
                k = 1
        if k > 1:
            newChar += str(k)

        return len(list(newChar))


if __name__ == '__main__':
    solution = Solution()
    assert solution.compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']) == 6