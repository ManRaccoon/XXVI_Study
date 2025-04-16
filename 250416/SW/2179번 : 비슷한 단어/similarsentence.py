'''
백준 2179번 문제, 비슷한 단어
https://www.acmicpc.net/problem/2179
'''

import sys

def common_prefix(a, b):
    length = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            length += 1
        else:
            break
    return length

def solve():
    N = int(sys.stdin.readline())
    words = []
    for idx in range(N):
        word = sys.stdin.readline().strip()
        words.append((word, idx))  # (단어, 입력순서)

    # 사전순 정렬
    sorted_words = sorted(words, key=lambda x: x[0])

    max_len = -1
    result = (-1, -1)  # (입력순서1, 입력순서2)

    for i in range(N - 1):
        word1, idx1 = sorted_words[i]
        word2, idx2 = sorted_words[i + 1]

        length = common_prefix(word1, word2)

        if length > max_len:
            max_len = length
            result = (idx1, idx2)
        elif length == max_len:
            # 입력 순서가 더 앞서는 쌍으로 업데이트
            if min(idx1, idx2) < min(result):
                result = (idx1, idx2)

    # 입력 순서 기준으로 다시 정렬해서 출력
    first, second = sorted([result[0], result[1]])
    print(words[first][0])
    print(words[second][0])

solve()
