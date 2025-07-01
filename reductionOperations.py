from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        S = 0
        min_ = nums[0]
        while nums[-1] != nums[0]:
            dummy = nums.pop()
            if dummy != nums[-1]:
                S += 1
                tail = nums[-1]
                nums.append(tail)

        return S


if __name__ == '__main__':
    solution = Solution()
    assert solution.reductionOperations([5, 1, 3]) == 3