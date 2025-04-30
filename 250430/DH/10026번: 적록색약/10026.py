from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visited_normal = [[False]*n for _ in range(n)]
visited_color_weak = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, is_weak):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    color = grid[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_weak:
                    if (color in 'RG' and grid[nx][ny] in 'RG') or color == grid[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:
                    if grid[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))

normal_count = 0
weak_count = 0

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            bfs(i, j, visited_normal, False)
            normal_count += 1

for i in range(n):
    for j in range(n):
        if not visited_color_weak[i][j]:
            bfs(i, j, visited_color_weak, True)
            weak_count += 1

print(normal_count, weak_count)
