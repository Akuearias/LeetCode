from typing import List

'''

LeetCode #131: Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(len(s) // 2 + 1):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        def backtrack(s: str, sub: str, bt_stack: List[str], palindromes: List[str]) -> None:
            if isPalindrome(sub):
                bt_stack.append(sub)
                palindromes.append(sub)
                backtrack(s, sub, bt_stack, palindromes)
                bt_stack.pop()

            else:
                return


        if len(s) == 1:
            return [[s]]

        bt_stack = []
        palindromes = []
        for i in range(1, len(s)):
            backtrack(s, s[0:i], bt_stack, palindromes)

# It says that backtracking is a solution, but I am not very familiar with how to build backtracking,
# though I know that backtracking is a kind of DFS.
if __name__ == '__main__': # Test cases
    solution = Solution()
    assert solution.partition("aab") == [['a', 'a', 'b'], ['aa', 'b']]
    assert solution.partition("a") == [['a']]