from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        S = 0
        for i, x in enumerate(nums):
            S += diff[i]
            x += S
            if x == 0:
                continue
            if x < 0 or i + k > n:
                return False

            S -= x
            diff[i + k] += x
        return True

# https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/solutions/2336744/chai-fen-shu-zu-pythonjavacgojs-by-endle-8qrt
