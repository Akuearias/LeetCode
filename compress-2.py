from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 1
        k = 1
        while j <= len(chars) - 1:
            if chars[j] == chars[j - 1]:
                k += 1
            else:
                if k > 1:
                    for n in range(len(str(k))):
                        chars[i + 1 + n] = str(k)[n]
                    i += len(str(k)) + 1
                else:
                    i += 1
                chars[i] = chars[j]
                k = 1
            j += 1

        if k > 1:
            for n in range(len(str(k))):
                chars[i + 1 + n] = str(k)[n]
            i += len(str(k)) + 1
        else:
            i += 1
        return i
