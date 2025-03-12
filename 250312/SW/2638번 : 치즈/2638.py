'''
백준 2638번 문제 : 치즈
https://www.acmicpc.net/problem/2638
'''

import sys
from collections import deque

#BFS를 통해 치즈가 아닌 부분을 공기로 만드는 함수
def bfs_external_air(board, N, M):
    external = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    external[0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not external[nx][ny]:
                # 공기인 경우에만 BFS 탐색 진행
                if board[nx][ny] == 0:
                    external[nx][ny] = True
                    queue.append((nx, ny))
    return external

#녹일 치즈를 정하는 함수
def melt_cheese(board, external, N, M):
    melt_list = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:  # 치즈인 경우
                count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        if external[ni][nj]:
                            count += 1
                if count >= 2:
                    melt_list.append((i, j))
    return melt_list

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    time = 0
    # 치즈가 남아 있는 동안 반복
    while True:
        external = bfs_external_air(board, N, M)
        melt_list = melt_cheese(board, external, N, M)
        
        if not melt_list:
            break
        
        for i, j in melt_list:
            board[i][j] = 0
        time += 1
    
    print(time)

if __name__ == '__main__':
    main()
