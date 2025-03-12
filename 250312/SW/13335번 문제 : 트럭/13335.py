'''
백준 13335분 문제 : 트럭
https://www.acmicpc.net/problem/13335
'''

from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n, bridge_length, max_weight = map(int, input().split())
    trucks = list(map(int, input().split()))
    
    time = 0
    current_weight = 0
    bridge = deque([0] * bridge_length)

    # 다리 큐가 비어있을 때까지 진행
    while bridge:
        time += 1
        # 다리 큐의 가장 왼쪽을 꺼내면서 현재 무게 조정
        current_weight -= bridge.popleft()
        
        # 아직 대기 중인 트럭이 있다면 다음 트럭을 다리에 올릴 수 있는지 확인
        if trucks:
            # 다리에 다음 트럭을 올렸을 때 무게 제한을 넘지 않는다면
            if current_weight + trucks[0] <= max_weight:
                truck = trucks.pop(0)  # 다음 트럭을 꺼내서
                bridge.append(truck)   # 다리의 오른쪽에 올리고
                current_weight += truck  # 현재 무게에 더하기
            else:
                # 무게 제한을 넘는다면, 빈 공간(0)을 다리 오른쪽에 추가
                bridge.append(0)
    print(time)

if __name__ == '__main__':
    main()
