import sys
import heapq

input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    p, r = map(int, input().split())
    li.append((p, r))
li.sort()
heap = []
for p, r in li:
    heapq.heappush(heap, r)
    if len(heap) > p:
        heapq.heappop(heap)

print(sum(heap))
