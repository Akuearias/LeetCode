import collections
from itertools import permutations
import math

class Solution:
    def isPrime(self, num: int) -> bool:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def minAnagramLength(self, s: str) -> int:
        if len(s) < 2:
            return 1
        if self.isPrime(len(s)):
            charList = list(set(s))
            if len(charList) == 1:
                return 1
            return len(s)
        anagrams = len(s)
        for i in range(1, int(len(s) / 2) + 1):
            if len(s) % i == 0:
                head = s[0:i]
                head_counter = collections.Counter(head)
                for j in range(i, len(s), i):
                    if collections.Counter(s[j:j+i]) != head_counter:
                        break
                    if j == len(s) - i:
                        anagrams = min(anagrams, i)
        return anagrams

solution = Solution()
print(solution.minAnagramLength('jjj'))

