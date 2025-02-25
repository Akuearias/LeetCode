class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_matrix = [[] for _ in range(numRows)]
        r = 0
        pos = True
        for i in range(len(s)):
            zigzag_matrix[r].append(s[i])
            if pos == True:
                r += 1
            elif pos == False:
                r -= 1
            if r == numRows - 1:
                pos = False
            if r == 0:
                pos = True
        S = ""
        for row in zigzag_matrix:
            S += "".join(row)
        return S

if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))