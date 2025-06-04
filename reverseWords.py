class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(' ')
        list2 = []
        for i in range(len(s_list)):
            if s_list[i] != '':
                list2.append(s_list[i])

        S = ''
        for i in range(len(list2) - 1, -1, -1):
            S += list2[i]
            if i != 0:
                S += ' '

        return S