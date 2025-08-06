from typing import List
import heapq


# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/solutions/1208350/cha-zhao-he-zui-xiao-de-kdui-shu-zi-by-l-z526
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        S = []
        m, n = len(nums1), len(nums2)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while heap and len(S) < k:
            _, i, j = heapq.heappop(heap)
            S.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return S