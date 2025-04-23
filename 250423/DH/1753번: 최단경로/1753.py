import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)
distance = [float('inf')] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])
