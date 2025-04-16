'''
백준 20437번 문제, 문자열 게임 2
https://www.acmicpc.net/problem/20437
'''

import sys
from collections import defaultdict

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        W = sys.stdin.readline().strip()
        K = int(sys.stdin.readline())
        
        pos = defaultdict(list)  # 각 알파벳의 등장 위치 저장

        for i, ch in enumerate(W):
            pos[ch].append(i)

        min_len = float('inf')
        max_len = -1

        for ch in pos:
            indices = pos[ch]
            if len(indices) < K:
                continue
            for i in range(len(indices) - K + 1):
                length = indices[i + K - 1] - indices[i] + 1
                min_len = min(min_len, length)
                max_len = max(max_len, length)

        if min_len == float('inf'):
            print(-1)
        else:
            print(f"{min_len} {max_len}")

solve()
