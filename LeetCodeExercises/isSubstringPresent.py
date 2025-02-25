class Solution:
    def reverse_string(self, s: str) -> str:
        s_rev = ''
        for i in range(0, int(len(s))):
            s_rev += s[len(s)-1-i]
        return s_rev

    def isSubstringPresent(self, s: str) -> bool:
        s_rev = self.reverse_string(s)
        dual_list = []
        for i in range(0, len(s) - 1):
            dual_list.append(s[i:i+2])
        B = False
        for dual in dual_list:
            if s_rev.__contains__(dual):
                B = True
                break
        return B
