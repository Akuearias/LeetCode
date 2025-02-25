from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letters = {"2": ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return num_letters[digits]
        else:
            all_strings = num_letters[digits[0]]
            i = 1
            while i < len(digits):
                all_strings = [s1 + s2 for s1 in all_strings for s2 in num_letters[digits[i]]]
                i += 1
            return all_strings

solution = Solution()
print(solution.letterCombinations('234'))
