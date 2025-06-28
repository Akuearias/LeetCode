class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Prefix Sum
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        # black: the number of black squares in column j+1
        # decreased=True: the number of black squares in column j+1 is less than that of column j+2
        @cache
        def DFS(j, black, decreased):
            if j < 0:
                return 0

            dummy = 0
            # Enumerate black squares in column j
            for b in range(n + 1):
                if b == black:  # Case 1: L==R
                    # No scores from squares
                    dummy = max(dummy, DFS(j - 1, b, False))

                elif b < black:  # Case 2: Right has more black squares
                    dummy = max(dummy, DFS(j - 1, b, True) + col_sum[j][black] - col_sum[j][b])

                elif not decreased:
                    dummy = max(dummy, DFS(j - 1, b, False) + col_sum[j + 1][b] - col_sum[j + 1][black])

                elif black == 0:
                    dummy = max(dummy, DFS(j - 1, b, False))

            return dummy

        return max(DFS(n - 2, i, False) for i in range(n + 1))

# https://leetcode.cn/problems/maximum-score-from-grid-operations/solutions/2852362/tu-jie-dp-ji-qi-you-hua-by-endlesscheng-pco6