class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        curr_round = min(min(xPos, yPos), min(num - xPos - 1, num - yPos - 1)) + 1

        s = (num - 2 * (curr_round - 1)) ** 2

        id_ = (num * num - s) % 9 + 1

        R = num - curr_round

        L = curr_round - 1

        if xPos == L:
            id_ += yPos - L

        elif yPos == R:
            id_ += R - L
            id_ += xPos - L

        elif xPos == R:
            id_ += 2 * (R - L)
            id_ += R - yPos

        else:
            id_ += 3 * (R - L)
            id_ += R - xPos

        return 9 if id_ % 9 == 0 else id_ % 9

# https://leetcode.cn/problems/SNJvJP/solutions/702546/gen-ju-mian-ji-qiu-chai-zhao-dao-suo-zai-06ih
