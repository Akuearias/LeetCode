class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                return 1

            else:
                count = 0
                for i in range(n):
                    if i in C or row - i in D1 or row + i in D2:
                        continue
                    C.add(i)
                    D1.add(row - i)
                    D2.add(row + i)
                    count += backtrack(row + 1)
                    C.remove(i)
                    D1.remove(row - i)
                    D2.remove(row + i)
                return count

        C = set()
        D1 = set()
        D2 = set()
        return backtrack(0)