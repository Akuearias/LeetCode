class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            str_n = str(n)
            S = 0
            for num in str_n:
                S += int(num) ** 2
            visited.add(n)
            n = S

        return False