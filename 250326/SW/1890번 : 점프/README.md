# 백준 1890번 점프 (실버 2티어)

## 문제 설명

NxN 크기의 격자판이 주어지고, 각 칸에는 이동할 수 있는 거리인 K가 적혀 있다. 시작점인 좌측 상단 (0,0)에서 도착점인 (N-1, N-1)에 도착할 때 까지 현재 칸에 적힌 숫자 K만큼 오른쪽 또는 아래쪽으로 점프할 수 있다. 이때 시작점에서 도착점까지 이동할 수 있는 모든 경로의 개수를 구해야한다.

## 해결 접근법

1. 각 칸에 도달하는 경로의 수를 저장하기 위해 2차원 DP배열을 사용했다.

2. 모든 칸에 대해 현재 칸의 경로 수가 0이 아니면, 해당 칸의 값 K를 확인했다.

3. K를 확인하고 오른쪽 또는 아래쪽으로 이동하며 DP배열에 값을 더해주며 도착점까지 반복했다.

4. 모든 칸을 순회하면 도착점에 저장된 값이 문제에서 요구하는 경로의 총 개수가 된다.

## 어려웠던 점

DP 개념이 오랜만이라 해맸지만 인터넷의 도움을 받아 개념을 이해하고 문제를 해결할 수 있었다.
