from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, s, sum_, curr):
            if sum_ >= target:
                if sum_ == target:
                    S.append(s[:])
                return

            i = curr
            while i < len(candidates):
                sum_ += candidates[i]
                s.append(candidates[i])
                backtrack(candidates, s, sum_, i)
                sum_ -= candidates[i]
                s.pop()
                i += 1

        S = []
        curr = 0
        backtrack(candidates, [], 0, curr)
        return S

