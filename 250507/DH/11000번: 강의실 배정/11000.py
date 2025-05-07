import heapq
import sys

n = int(sys.stdin.readline())
lectures = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
lectures.sort()

heap = []
heapq.heappush(heap, lectures[0][1])
for i in range(1, n):
    if heap[0] <= lectures[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lectures[i][1])

print(len(heap))
