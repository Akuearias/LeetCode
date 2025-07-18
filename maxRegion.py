def maxRegion(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] == 0 or visited[r][c]:
            return 0

        visited[r][c] = True
        size = 1
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    size += dfs(r + dr, c + dc)
        return size

    max_region = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                max_region = max(max_region, dfs(r, c))

    return max_region