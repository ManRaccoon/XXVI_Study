from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, s):
    d_visited[s] = True
    print(s, end=" ")
    for i in graph[s]:
        if d_visited[i] == False:
            dfs(graph, i)

def bfs(graph, s):
    queue = deque([s])
    b_visited[s] = True
    while queue:
        result = queue.popleft()
        print(result, end=" ")
        for i in graph[result]:
            if b_visited[i] == False:
                b_visited[i] = True
                queue.append(i)

vertex, edge, s = map(int, input().split()) 

graph=[[] for _ in range(vertex + 1)]

d_visited = [False for _ in range(vertex + 1)]
b_visited = [False for _ in range(vertex + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(vertex + 1):
    graph[i].sort()

dfs(graph, s)
print()
bfs(graph, s)
