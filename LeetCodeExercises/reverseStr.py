class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            for i in range(0, len(s)//2):
                dummy = s[i]
                s[i] = s[len(s)-i-1]
                s[len(s)-i-1] = dummy
            return s

        s = list(s)
        sub_len = 2 * k
        i = 0
        new_list = []
        while i < len(s):
            new_list.append(''.join(reverse(s[i:i+k])))
            new_list.append(''.join(s[i+k:i+2*k]))
            i += sub_len

        return ''.join(new_list)

solution = Solution()
print(solution.reverseStr("abcdefghijklmnopqrs", 4))