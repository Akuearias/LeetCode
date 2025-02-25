class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        nums = [f"{num:04}" for num in nums]

        num_string = ''
        for i in range(0, 4):
            num_string += str(min(min(int(nums[0][i]), int(nums[1][i])), int(nums[2][i])))
        return int(num_string)


nums = [1, 10, 1000]
solution = Solution()
print(solution.generateKey(1, 10, 1000))

