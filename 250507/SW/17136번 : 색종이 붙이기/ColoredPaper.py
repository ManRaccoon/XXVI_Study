import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
paper = [0] + [5] * 5
min_count = float('inf')

def can_attach(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != 1:
                return False
    return True

def set_paper(x, y, size, value):
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = value

def dfs(pos, count):
    global min_count
    if count >= min_count:
        return
    if pos == 100:
        min_count = min(min_count, count)
        return
    x = pos // 10
    y = pos % 10
    if board[x][y] == 1:
        for size in range(5, 0, -1):
            if paper[size] > 0 and can_attach(x, y, size):
                set_paper(x, y, size, 0)
                paper[size] -= 1
                dfs(pos + 1, count + 1)
                paper[size] += 1
                set_paper(x, y, size, 1)
    else:
        dfs(pos + 1, count)

dfs(0, 0)
print(min_count if min_count != float('inf') else -1)
