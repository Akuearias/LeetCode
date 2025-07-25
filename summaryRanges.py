from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        l = 0
        S = []
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                if l != i - 1:
                    dummy = f"{nums[l]}->{nums[i - 1]}"
                else:
                    dummy = f"{nums[l]}"
                S.append(dummy)
                l = i

        if l != n - 1:
            dummy = f"{nums[l]}->{nums[n - 1]}"
        else:
            dummy = f"{nums[l]}"
        S.append(dummy)
        return S