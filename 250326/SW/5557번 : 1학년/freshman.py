'''
백준 5557번 문제. 1학년
https://www.acmicpc.net/problem/5557
'''

import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    nums = list(map(int, input().split()))
    
    # dp[i][j]: 첫 번째 수부터 i번째 수까지 사용하여 결과가 j가 되는 경우의 수
    # 연산에 사용되는 수는 총 N-1개이므로, dp 테이블은 N-1 행과 21(0~20) 열을 사용
    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][nums[0]] = 1
    
    # 수열의 두 번째 원소부터 N-1번째 원소까지 연산 수행 (마지막 숫자는 목표값)
    for i in range(1, n - 1):
        for j in range(21):
            if dp[i - 1][j] != 0:
                plus = j + nums[i]
                minus = j - nums[i]
                if plus <= 20:
                    dp[i][plus] += dp[i - 1][j]
                if minus >= 0:
                    dp[i][minus] += dp[i - 1][j]
    
    # 목표값은 수열의 마지막 숫자: nums[-1]
    print(dp[n - 2][nums[-1]])

if __name__ == "__main__":
    main()
