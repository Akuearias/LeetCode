# There are n stairs, you can climb either one stair or two stairs. How many methods are there?
def climbStairs(n: int) -> int:
    if n < 2:
        return 1

    p1, p2 = 1, 1
    for i in range(2, n + 1):
        current = p1 + p2
        p2 = p1
        p1 = current

    return p1


if __name__ == '__main__':
    print(climbStairs(20))