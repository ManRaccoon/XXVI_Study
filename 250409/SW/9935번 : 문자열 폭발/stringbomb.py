'''
백준 9935번 문제, 문자열 폭발
https://www.acmicpc.net/problem/9935
'''

import sys

def main():
    input = sys.stdin.readline
    s = input().rstrip('\n')
    bomb = input().rstrip('\n')
    bomb_len = len(bomb)
    
    stack = []
    
    # S의 각 문자를 순회
    for char in s:
        stack.append(char)
        # 스택에 쌓인 문자의 길이가 폭발 문자열보다 크거나 같을 때, 스택의 끝 부분이 폭발 문자열과 동일한지 확인
        if len(stack) >= bomb_len:
            if ''.join(stack[-bomb_len:]) == bomb:
                # 동일하면 해당 부분 스택에서 제거
                del stack[-bomb_len:]
    
    result = ''.join(stack)
    # 결과 문자열이 비어 있으면 "FRULA" 출력
    if result:
        print(result)
    else:
        print("FRULA")

if __name__ == '__main__':
    main()
