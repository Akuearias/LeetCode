class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2

# https://leetcode.cn/problems/reach-a-number/solutions/1946020/dao-da-zhong-dian-shu-zi-by-leetcode-sol-ak90
