n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_repaint(x, y):
    repaint_w = 0  # W로 시작
    repaint_b = 0  # B로 시작
    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            # 기준 체스판의 색상은 (i+j)%2가 0이면 시작색, 1이면 반대색
            if (i + j) % 2 == 0:
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
    return min(repaint_w, repaint_b)

min_repaint = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        min_repaint = min(min_repaint, count_repaint(i, j))

print(min_repaint)
