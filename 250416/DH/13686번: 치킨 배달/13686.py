import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

result = float('inf')

for i in combinations(chickens, m):
    total = 0
    for hx, hy in houses:
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in i)
        total += dist
    result = min(result, total)

print(result)
