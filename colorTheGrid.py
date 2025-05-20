'''

LeetCode Exercise #1931. Painting a Grid With Three Different Colors
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 10^9 + 7.



Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986


Constraints:

1 <= m <= 5
1 <= n <= 1000


'''


# Key point: Dynamic Programming
# This is a famous NP-Complete problem, and thus the conventional DP does not work.
# Even if DP works, the time complexity will become awful: O(n * 3^(2*m))
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        valid = {}

        for mask in range(3 ** m):
            color = []
            dummy = mask
            for i in range(m):
                color.append(dummy % 3)
                dummy //= 3

            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        adj = defaultdict(list)
        for m1, c1 in valid.items():
            for m2, c2 in valid.items():
                if not any(x == y for x, y in zip(c1, c2)):
                    adj[m1].append(m2)

        f = [int(mask in valid) for mask in range(3 ** m)]
        for i in range(1, n):
            g = [0] * (3 ** m)
            for m2 in valid.keys():
                for m1 in adj[m2]:
                    g[m2] += f[m1]
                    if g[m2] >= (10 ** 9 + 7):
                        g[m2] -= (10 ** 9 + 7)

            f = g

        return sum(f) % (10 ** 9 + 7)


