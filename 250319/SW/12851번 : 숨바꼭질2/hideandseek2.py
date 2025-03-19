'''
백준 12851번 문제. 숨바꼭질 2
https://www.acmicpc.net/problem/12851
'''

from collections import deque
import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    
    MAX = 100000
    dist = [float('inf')] * (MAX + 1)
    ways = [0] * (MAX + 1)
    
    queue = deque()
    # 초기 위치 설정: 수빈이의 위치 N
    dist[N] = 0
    ways[N] = 1
    queue.append(N)
    
    while queue:
        current = queue.popleft()
        # 가능한 세 가지 이동
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= MAX:
                # 처음 방문한 경우
                if dist[next_pos] == float('inf'):
                    dist[next_pos] = dist[current] + 1
                    ways[next_pos] = ways[current]
                    queue.append(next_pos)
                # 이미 같은 최소 시간으로 도달한 경우, 경로 수를 누적
                elif dist[next_pos] == dist[current] + 1:
                    ways[next_pos] += ways[current]
    
    print(dist[K])
    print(ways[K])

if __name__ == "__main__":
    main()
