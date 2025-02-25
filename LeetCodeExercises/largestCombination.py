from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        if len(candidates) < 2:
            return len(candidates)


        bin_len = len(bin(10**7)[2:])
        bins = []

        for i in range(0, len(candidates)):
            bins.append(bin(candidates[i])[2:].zfill(bin_len))

        ones = []
        for i in range(bin_len):
            one = 0
            for j in range(len(bins)):
                if bins[j][i] == '1':
                    one += 1
                ones.append(one)
        return max(ones)


solution = Solution()
print(solution.largestCombination([8, 8]))




