from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        work_floors = []
        low = bottom
        for sp in special:
            work_floors.append(range(low, sp))
            low = sp + 1

        work_floors.append(range(low, top + 1))

        return max(list(map(len, work_floors)))

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxConsecutive(6, 8, [7, 6, 8]))