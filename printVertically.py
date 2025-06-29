from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words_list = s.split(' ')
        longest = 0
        longest_id = 0
        for i in range(len(words_list)):
            longest = max(longest, len(words_list[i]))
        vertical = []
        for i in range(longest):
            vertical_word = []
            for j in range(len(words_list)):
                if i < len(words_list[j]):
                    vertical_word.append(words_list[j][i])
                else:
                    vertical_word.append(" ")
            vertical_str = ''.join(vertical_word)
            vertical_str = vertical_str.rstrip()
            vertical.append(vertical_str)

        return vertical
