class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        for x in range(x1, x2 + 1, 1):
            for y in range(y1, y2 + 1, 1):
                if (x-xCenter)**2 + (y-yCenter)**2 <= radius**2:
                    return True
        return False

if __name__ == "__main__":
    radius = 1
    xCenter = 0
    yCenter = 0
    x1 = 1
    y1 = -1
    x2 = 3
    y2 = 1
    print(Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))