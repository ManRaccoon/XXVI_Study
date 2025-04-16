import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
result = []

n = int(input())

for _ in range(n):
    cmd = input().strip().split()
    
    if cmd[0] == '1':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        dq.append(int(cmd[1]))
    elif cmd[0] == '3':
        if dq:
            result.append(str(dq.popleft()))
        else:
            result.append('-1')
    elif cmd[0] == '4':
        if dq:
            result.append(str(dq.pop()))
        else:
            result.append('-1')
    elif cmd[0] == '5':
        result.append(str(len(dq)))
    elif cmd[0] == '6':
        result.append('0' if dq else '1')
    elif cmd[0] == '7':
        if dq:
            result.append(str(dq[0]))
        else:
            result.append('-1')
    elif cmd[0] == '8':
        if dq:
            result.append(str(dq[-1]))
        else:
            result.append('-1')

print('\n'.join(result))
