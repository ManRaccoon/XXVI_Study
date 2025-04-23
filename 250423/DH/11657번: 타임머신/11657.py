import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distance = [INF] * (n + 1)
distance[1] = 0  # 시작 도시

def bellman_ford():
    for i in range(n - 1):
        for u, v, w in edges:
            if distance[u] != INF and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] != INF and distance[v] > distance[u] + w:
            return False
    return True

if bellman_ford():
    for i in range(2, n + 1):
        print(distance[i] if distance[i] != INF else -1)
else:
    print(-1)
