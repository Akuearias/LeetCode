class Solution:
    def stringHash(self, s: str, k: int) -> str:
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        new_string = ''
        index = 0
        while index < len(s):
            string = s[index:index+k]
            S = 0
            for char in string:
                S += nums[chars.index(char)]
            S = S % 26
            S = chars[nums.index(S)]
            new_string += S
            index += k
        return new_string


solution = Solution()
print(solution.stringHash("mxz", 3))
