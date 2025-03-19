def dfs(graph, visited, st):
  visited[st] = True
  count = 1
  for i in graph[st]:
    if visited[i] == False:
      count += dfs(graph, visited, i)
  return count
vertex = int(input())
edge = int(input())
visited = [False for _ in range(vertex + 1)]
graph = [[] for _ in range(vertex + 1)]
for _ in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
print(dfs(graph, visited, 1) - 1)
