from typing import List


class Solution:
    def combinationSumHelper(self, candidate, candidates, i, available, comb, target):
        for cand in candidates:
            if sum(comb) + cand > target:
                comb.pop()
                continue
            elif sum(comb) + candidates[i] == target:
                comb.append(candidates[i])
                available.append(comb)
                return
            else:
                comb.append(candidates[i])
                self.combinationSumHelper(candidate, candidates, i, available, comb, target)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        available = []
        for candidate in candidates:
            comb = []
            i = candidates.index(candidate)
            candidates = candidates[candidates.index(candidate):]
            self.combinationSumHelper(candidate, candidates, i, available, comb, target)

        return available


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([8,7,4,3], 11))