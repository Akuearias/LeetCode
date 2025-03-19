'''

LeetCode Exercise #3305. Count of Substrings Containing Every Vowel and K Consonants I

You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.



Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".


Constraints:

5 <= word.length <= 250
word consists only of lowercase English letters.
0 <= k <= word.length - 5

'''
import collections


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        letter_count = dict(collections.Counter(word))
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            if vowel not in letter_count.keys():
                return 0

        vc = []
        for letter in word:
            if letter in vowels:
                vc.append(letter)
            else:
                vc.append('c')

        S = 0
        letters_count = collections.defaultdict(int)
        consonants = 0

        i = 0
        while i < len(vc) - 5 - k + 1:
            j = i
            while j < len(vc):
                if vc[j] == 'a':
                    letters_count['a'] += 1
                elif vc[j] == 'e':
                    letters_count['e'] += 1
                elif vc[j] == 'i':
                    letters_count['i'] += 1
                elif vc[j] == 'o':
                    letters_count['o'] += 1
                elif vc[j] == 'u':
                    letters_count['u'] += 1
                else:
                    if consonants < k:
                        consonants += 1
                    else:
                        break
                j += 1

            all_true = True
            for flag in flags:
                if not flag:
                    all_true = False

            if all_true:
                S += 1

            i += 1
            j = i
            flags = [False, False, False, False, False]
            consonants = 0

        return S


if __name__ == '__main__':
    solution = Solution()
    assert solution.countOfSubstrings('aeioqq', 1) == 0
    assert solution.countOfSubstrings('aeiou', 0) == 1
    assert solution.countOfSubstrings('ieaouqqieaouqq', 1) == 3
    assert solution.countOfSubstrings('iqeaouqi', 2) == 3