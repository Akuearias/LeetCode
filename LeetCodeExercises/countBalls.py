import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        digit_sums = []
        for i in range(lowLimit, highLimit + 1):
            string_num = str(i)
            S = 0
            for s in string_num:
                S += int(s)
            digit_sums.append(S)

        digit_sums_counts = list(dict(collections.Counter(digit_sums)).values())

        count_index = digit_sums_counts.index(max(digit_sums_counts))
        return digit_sums_counts[count_index]

if __name__ == '__main__':
    solution = Solution()
    print(solution.countBalls(1, 10))
