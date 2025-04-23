from collections import deque

# 입력 받기
board = [list(input()) for _ in range(12)]

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = board[x][y]
    puyos = [(x, y)]

    while queue:
        cx, cy = queue.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    puyos.append((nx, ny))
    return puyos

def apply_gravity():
    for col in range(6):
        stack = []
        for row in range(11, -1, -1):  # 아래에서 위로
            if board[row][col] != '.':
                stack.append(board[row][col])
        for row in range(11, -1, -1):
            if stack:
                board[row][col] = stack.pop(0)
            else:
                board[row][col] = '.'

# 메인 로직
chain_count = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    is_popped = False

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    is_popped = True
                    for x, y in group:
                        board[x][y] = '.'

    if not is_popped:
        break
    apply_gravity()
    chain_count += 1

print(chain_count)
