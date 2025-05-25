'''

LeetCode Exercise #30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:

1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

'''
import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # For this part of code, though it is correct, it is more Brute-Force than Sliding Window.
        # Time Complexity: O(N * M^2).
        total = 0
        each = len(words[0])
        for word in words:
            total += len(word)

        target = dict(collections.Counter(words))
        matching = []
        i = 0
        while i < len(s) - total + 1:
            L = i
            R = L + each
            current_dict = collections.defaultdict(str)
            while R <= i + total:
                sub = s[L:R]
                if sub in target:
                    k = sub
                    if current_dict.get(k, 0) < target[k]:
                        current_dict[k] = current_dict.get(k, 0) + 1
                        L += each
                        R += each
                    else:
                        break
                else:
                    break

            if R == i + total + each:
                matching.append(i)
            i += 1

        return matching

    # This is the reference solution. Some variable names are modified. Time complexity: O(n^2)
    # Portal to the solution:
    # https://leetcode.cn/problems/substring-with-concatenation-of-all-words/solutions/1616997/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-244a/
    def findSubstring_ref_answer(self, s: str, words: List[str]) -> List[int]:
        matching = []
        total, each, len_str = len(words), len(words[0]), len(s)
        for i in range(each):
            if i + total * each > len_str: # What's this? The instruction of the solution to this problem is too vague.
                break

            diff = collections.Counter()
            for j in range(total):
                dummy = s[i + j * each : i + (j + 1) * each]
                diff[dummy] += 1

            for word in words:
                diff[word] -= 1
                if diff[word] == 0:
                    del diff[word]

            for L in range(i, len_str - total * each + 1, each):
                if L != i:
                    word = s[L + (total - 1) * each : L + total * each]
                    diff[word] += 1
                    if diff[word] == 0:
                        del diff[word]

                    word = s[L - each : L]
                    diff[word] -= 1

                    if diff[word] == 0:
                        del diff[word]

                if len(diff) == 0:
                    matching.append(L)

        return matching

if __name__ == '__main__':
    solution = Solution()
    assert solution.findSubstring('barfoothefoobarman', ['bar', 'foo']) == [0, 9]
    assert solution.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]) == []
    assert solution.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]) == [6, 9, 12]

