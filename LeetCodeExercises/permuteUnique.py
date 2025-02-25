from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(id, perm, n, results, dummy):
            if id == n:
                results.append(perm)
                return
            else:
                if id not in dummy:
                    perm.append(nums[id])
                    dummy.append(id)
