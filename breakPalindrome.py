'''

LeetCode #1328: Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.


Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.

'''

import collections


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        elif not palindrome.__contains__('a'):
            return "a" + palindrome[1:]

        else:
            if list(dict(collections.Counter(palindrome)).keys()) == ['a']:
                return palindrome[:len(palindrome) - 1] + 'b'

            else:
                if palindrome[0] != 'a':
                    return 'a' + palindrome[1:]

                else:
                    letters_count = dict(collections.Counter(palindrome))
                    if letters_count['a'] == len(palindrome) - 1:
                        return palindrome[:len(palindrome) - 1] + 'b'
                    else:
                        for i in range(len(palindrome) // 2):
                            if palindrome[i] != 'a':
                                return palindrome[:i] + 'a' + palindrome[i + 1:]



if __name__ == '__main__':
    solution = Solution()
    assert solution.breakPalindrome("abccba") == "aaccba"
    assert solution.breakPalindrome('a') == ""

