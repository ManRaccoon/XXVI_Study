'''
백준 1141번 문제, 접두사
https://www.acmicpc.net/problem/1141
'''

import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    
    # set자료형을 통해 단어 중복 제거 후 리스트로 변환
    words = list(set(input().split()))
    
    # 사전순 정렬을 통해 접두어 관계인 단어들이 인접하게 위치됨
    words.sort()
    
    count = 0
    for i in range(len(words)):
        # 다음 단어가 존재하고, 현재 단어가 다음 단어의 접두어인 경우
        if i < len(words) - 1 and words[i+1].startswith(words[i]):
            continue  # 접두어이면 포함하지 않음
        count += 1  # 아니라면 결과에 포함
    
    print(count)

if __name__ == '__main__':
    main()
