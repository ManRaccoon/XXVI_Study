'''
백준 1890번 문제. 점프
https://www.acmicpc.net/problem/1890
'''

import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(n)]
  
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            # 현재 칸까지 도달하는 경로가 없거나, 도착 칸이면 넘어감
            if dp[i][j] == 0 or (i == n-1 and j == n-1):
                continue
            jump = board[i][j]
            # 오른쪽으로 점프
            if j + jump < n:
                dp[i][j + jump] += dp[i][j]
            # 아래쪽으로 점프
            if i + jump < n:
                dp[i + jump][j] += dp[i][j]
    
    print(dp[n-1][n-1])

if __name__ == "__main__":
    main()
