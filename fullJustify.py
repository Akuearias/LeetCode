# https://leetcode.cn/problems/text-justification/solutions/986756/wen-ben-zuo-you-dui-qi-by-leetcode-solut-dyeg
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        S = []
        r, n = 0, len(words)
        while True:
            l = r
            s = 0

            while r < n and s + len(words[r]) + r - l <= maxWidth:
                s += len(words[r])
                r += 1

            if r == n:
                dummy = ' '.join(words[l:])
                S.append(dummy + ' ' * (maxWidth - len(dummy)))
                break

            numWords = r - l
            numSpaces = maxWidth - s

            if numWords == 1:
                S.append(words[l] + numSpaces * ' ')
                continue

            averageSpaces = numSpaces // (numWords - 1)
            remain = numSpaces % (numWords - 1)
            space1 = ' ' * (averageSpaces + 1)
            space2 = ' ' * averageSpaces
            s1 = space1.join(words[l:l + remain + 1])
            s2 = space2.join(words[l + remain + 1:r])
            S.append(s1 + ' ' * averageSpaces + s2)

        return S