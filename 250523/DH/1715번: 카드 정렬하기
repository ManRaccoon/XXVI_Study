import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []
result = 0
for i in range(N):
    num = int(input())
    heapq.heappush(h, num)
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    c = a + b
    result += c
    heapq.heappush(h, c)
print(result)
