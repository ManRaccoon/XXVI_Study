# 백준 17086번 아기상어2 (골드 5티어)

## 문제 설명

문제에서는 N×M 크기의 격자가 주어지며, 격자의 각 칸에는 아기 상어(1) 또는 빈 칸(0)이 들어있다. 각 빈 칸의 안전 거리는 그 칸에서 가장 가까운 아기 상어까지의 최단 거리(대각선 이동 포함, 총 8방향 이동 가능)로 정의됩니다. 문제의 목표는 전체 격자에서 가장 큰 안전 거리를 리턴해야한다.

## 해결 접근법

1. 격자 내의 모든 아기 상어가 위치한 칸을 BFS의 시작점으로 설정한 Multi-Source BFS 알고리즘을 활용했다.

2. 각 아기 상어 위치에서 출발하여 아직 방문하지 않은 칸에 대해, 현재 칸의 거리 +1을 계산하여 저장하고 큐에 추가했다.

3. BFS의 특성상 각 칸은 가장 가까운 아기 상어로부터의 최단 거리로 채워진다.

4. BFS가 모두 종료된 후 전체 격자에서 최대 값을 찾아 리턴했다.

## 어려웠던 점

모든 칸에 아기상어가 존재하는 경우, 즉 최대 안전 거리가 0인 경우를 생각하지 못해 해맸다.
