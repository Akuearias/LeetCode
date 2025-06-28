import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_dict = dict(collections.Counter(nums))
        nums_set = list(nums_dict.keys())
        points = [0] * len(nums_set)
        points[0] = nums_set[0] * nums_dict[nums_set[0]]
        for i in range(1, len(nums_set)):
            if nums_set[i] != nums_set[i - 1] + 1:
                points[i] = points[i - 1] + nums_dict[nums_set[i]] * nums_set[i]
            else:
                if i - 2 >= 0:
                    points[i] = max(max(points[i - 2] + nums_dict[nums_set[i]] * nums_set[i], nums_set[i] * nums_dict[nums_set[i]]), points[i - 1])
                else:
                    points[i] = max(points[i - 1], nums_set[i] * nums_dict[nums_set[i]])

        return max(points)


if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteAndEarn([1,1,1,2,4,5,5,5,6]))
