from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    # Dir: up-0, down-1, l-2, r-3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    queue = deque()

    # Initializing the total steps as 0, in 4 dirs
    for d in range(4):
        dist[startX][startY][d] = 0
        queue.append((startX, startY, d, 0))

    while queue:
        x, y, d, steps = queue.popleft()
        nx, ny = x + dx[d], y + dy[d]
        # Continue the current direction without adding steps
        while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X':
            if dist[nx][ny][d] > steps:
                dist[nx][ny][d] = steps
                queue.appendleft((nx, ny, d, steps))  # Handled first
            nx += dx[d]
            ny += dy[d]
        # Turn (steps + 1)
        for new_d in range(4):
            if new_d != d and dist[x][y][new_d] > steps + 1:
                dist[x][y][new_d] = steps + 1
                queue.append((x, y, new_d, steps + 1))

    return min(dist[goalX][goalY]) + 1