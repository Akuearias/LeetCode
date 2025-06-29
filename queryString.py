class Solution:
    def queryString(self, s: str, n: int) -> bool:
        bins = set()
        bin_len = len(bin(n)) - 2

        for i in range(1, bin_len + 1):
            for j in range(len(s) - i + 1):
                sub = s[j:j+i]
                if sub[0] == '0':
                    continue
                num = int(sub, 2)
                if 1 <= num <= n:
                    bins.add(num)

        return len(bins) == n

# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/solutions/2264108/zi-chuan-neng-biao-shi-cong-1-dao-n-shu-ojtz8