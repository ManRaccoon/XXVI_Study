'''
백준 17086번 문제. 아기상어2
https://www.acmicpc.net/problem/17086
'''

from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    # 거리 정보를 저장할 배열 (방문하지 않은 칸은 -1로 초기화)
    dist = [[-1] * m for _ in range(n)]
    
    queue = deque()
    # 모든 아기 상어의 위치를 초기 BFS 큐에 추가
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                queue.append((i, j))
                
    # 8방향 (상, 하, 좌, 우, 대각선 4방향) 이동 좌표
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),           (0, 1), 
                  (1, -1),  (1, 0),  (1, 1)]
    
    # BFS 수행
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 격자 범위 내이며 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    # 전체 격자에서 최대 안전 거리를 계산
    answer = max(max(row) for row in dist)
    print(answer)

if __name__ == "__main__":
    main()
