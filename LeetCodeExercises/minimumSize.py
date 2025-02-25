from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        ans = 0
        while l < r:
            y = (l + r) // 2
            oper = 0
            for i in range(len(nums)):
                oper += (nums[i] - 1) // y
            if oper <= maxOperations:
                ans = y
                r -= 1
            else:
                l += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSize(nums=[2,4,8,2], maxOperations=4))
