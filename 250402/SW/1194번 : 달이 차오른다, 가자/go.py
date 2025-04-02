'''
백준 1194번 문제. 달이 차오른다, 가자
https://www.acmicpc.net/problem/1194
'''

from collections import deque
import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    maze = [list(input().strip()) for _ in range(N)]
    
    # 시작점 찾기
    start_x, start_y = 0, 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '0':
                start_x, start_y = i, j
                break
    
    # 3차원 방문 배열 [행][열][열쇠 상태]
    visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((start_x, start_y, 0, 0))  # (x, y, 현재 열쇠 상태, 이동 횟수)
    visited[start_x][start_y][0] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y, keys, steps = queue.popleft()
        
        # 도착지 '1'을 만나면 현재 이동 횟수를 출력 후 종료
        if maze[x][y] == '1':
            print(steps)
            return
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                cell = maze[nx][ny]
                # 벽(#)이면 이동 불가
                if cell == '#':
                    continue
                
                new_keys = keys
                # 키를 만난 경우 해당 키를 보유 상태에 추가
                if 'a' <= cell <= 'f':
                    new_keys = keys | (1 << (ord(cell) - ord('a')))
                
                # 문을 만난 경우 해당 키가 없다면 이동 불가
                if 'A' <= cell <= 'F':
                    if not (keys & (1 << (ord(cell) - ord('A')))):
                        continue
                
                if not visited[nx][ny][new_keys]:
                    visited[nx][ny][new_keys] = True
                    queue.append((nx, ny, new_keys, steps + 1))
                    
    # 탈출구를 찾지 못한 경우 -1 출력
    print(-1)

if __name__ == '__main__':
    main()
