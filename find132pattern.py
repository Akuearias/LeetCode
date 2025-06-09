from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        max_k = float('-inf')  # record the max nums_k

        for i in range(len(nums) - 1, -1, -1):  # Traverse from R to L
            if nums[i] < max_k:
                return True  # This means we find a legal 1-3-2.
            while stack and stack[-1] < nums[i]:
                max_k = stack.pop()  # This value may become max_k
            stack.append(nums[i])  # Potential nums[j]

        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.find132pattern([1, 2, 3, 4]) == False
    assert solution.find132pattern([3, 1, 4, 2]) == True
    assert solution.find132pattern([-1, 3, 2, 0]) == True
    print(solution.find132pattern([1, 3, 4, 2]))
    print(solution.find132pattern([3, 4, 5, 1]))