from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        def Backtrack(nums, visited, s, n):
            if len(s) == n:
                S.add(tuple(s))
                return

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue

                s.append(nums[i])
                visited.add(nums[i])
                Backtrack(nums, visited, s, n)
                s.pop()
                visited.remove(nums[i])

        S = set()
        n = len(nums)
        total = n * (n - 1)
        visited = set()
        Backtrack(nums, visited, [], n)

        S = list(S)
        for i in range(total):
            S[i] = list(S[i])

        return S

