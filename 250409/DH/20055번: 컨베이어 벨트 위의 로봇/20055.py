import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
con = deque(map(int, input().split()))
is_robot = deque([False] * N)

cnt = 0

while True:
  cnt += 1

  # 1단계 : 한 칸 회전
  con.rotate(1)
  is_robot.rotate(1)
  is_robot[-1] = False

  # 2단계 : 회전하는 방향으로 한칸 이동할 수 있다면 이동한다.
  for i in range(N-2, -1, -1):
    if is_robot[i] and not is_robot[i+1] and con[i+1] > 0:
      con[i+1] -= 1
      is_robot[i] = False
      is_robot[i+1] = True
  is_robot[-1] = False

  # 3단계 : 올리는 칸의 내구도가 0이 아니면 로봇을 올린다.
  if con[0] > 0:
    is_robot[0] = True
    con[0] -= 1
  
  # 4단계 : 내구도 0인 칸의 개수 K개 이상 -> 종료
  if con.count(0) >= K:
    break

print(cnt)
