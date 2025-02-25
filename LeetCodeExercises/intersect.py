import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def compare(num1: List[int], num2: List[int]) -> List[int]:
            nums1_count = dict(collections.Counter(nums1))
            nums2_count = dict(collections.Counter(nums2))

            intersection = []
            for i in nums1_count:
                if i in nums2_count:
                    intersection += [i] * min(nums1_count[i], nums2_count[i])

            return intersection

        if len(nums1) > len(nums2):
            return compare(nums1, nums2)
        else:
            return compare(nums2, nums1)


solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))
