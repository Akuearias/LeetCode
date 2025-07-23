class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalnum():
                s1 += char.lower()

        if len(s1) <= 1:
            return True

        else:
            stack = []
            if len(s1) % 2 == 0:
                for i in range(len(s1)):
                    if i < len(s1) // 2:
                        stack.append(s1[i])
                    else:
                        dummy = stack.pop()
                        if dummy != s1[i]:
                            return False
                return True

            else:
                for i in range(len(s1)):
                    if i < len(s1) // 2:
                        stack.append(s1[i])
                    elif i > len(s1) // 2:
                        dummy = stack.pop()
                        if dummy != s1[i]:
                            return False
                return True
