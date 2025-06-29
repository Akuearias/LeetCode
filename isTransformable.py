import collections


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if collections.Counter(s) != collections.Counter(t):
            return False

        s_len = len(s)
        positions = {i: collections.deque() for i in range(10)}
        for i, d in enumerate(s):
            positions[int(d)].append(i)

        for i, d in enumerate(t):
            d = int(d)

            if any(positions[j] and positions[j][0] < positions[d][0] for j in range(d)):
                return False
            positions[d].popleft()

        return True

# https://leetcode.cn/problems/check-if-string-is-transformable-with-substring-sort-operations/solutions/412892/jian-cha-zi-fu-chuan-shi-fou-ke-yi-tong-guo-pai-2
