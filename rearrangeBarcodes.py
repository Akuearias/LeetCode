import collections
import heapq
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcode_counts = collections.Counter(barcodes)
        pq = []

        for barcode, barcode_count in barcode_counts.items():
            heapq.heappush(pq, (-barcode_count, barcode))

        S = []
        while pq:
            barcode_count, barcode = heapq.heappop(pq)
            if len(S) == 0 or S[-1] != barcode:
                S.append(barcode)
                if barcode_count < -1:
                    heapq.heappush(pq, (barcode_count + 1, barcode))

            else:
                barcode_count_2, barcode_2 = heapq.heappop(pq)
                S.append(barcode_2)
                if barcode_count_2 < -1:
                    heapq.heappush(pq, (barcode_count_2 + 1, barcode_2))

                heapq.heappush(pq, (barcode_count, barcode))

        return S

# https://leetcode.cn/problems/distant-barcodes/solutions/2267110/ju-chi-xiang-deng-de-tiao-xing-ma-by-lee-31qt
