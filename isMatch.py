'''

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

'''

# Labels: Dynamic programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i1, i2):
            if i1 == 0:
                return False
            if p[i2 - 1] == '.':
                return True

            return s[i1 - 1] == p[i2 - 1]

        m, n = len(s), len(p)
        DP = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        DP[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    DP[i][j] |= DP[i][j - 2] # Won't j be out of range (1 - 2 = -1)?
                    if match(i, j - 1):
                        DP[i][j] |= DP[i - 1][j]

                else:
                    if match(i, j):
                        DP[i][j] |= DP[i - 1][j - 1]

        return DP[m][n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isMatch("aa", "a") == False
    assert solution.isMatch("aa", "a*") == True
    assert solution.isMatch("ab", ".*") == True


        
