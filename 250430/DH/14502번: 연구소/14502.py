from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus(temp_lab):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_lab[nx][ny] == 0:
                    temp_lab[nx][ny] = 2
                    q.append((nx, ny))

def get_safe_area(temp_lab):
    return sum(row.count(0) for row in temp_lab)

max_safe = 0

for walls in combinations(empty, 3):
    temp = copy.deepcopy(lab)
    for x, y in walls:
        temp[x][y] = 1
    spread_virus(temp)
    max_safe = max(max_safe, get_safe_area(temp))

print(max_safe)
