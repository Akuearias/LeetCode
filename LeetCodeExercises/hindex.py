from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        H = 0
        k = 0
        total_papers = len(citations)
        for i in range(0, total_papers):
            for paper in citations:
                if paper >= i:
                    k += 1

            if k >= i:
                H = max(H, i)

        return H

solution = Solution()
print(solution.hIndex([1]))