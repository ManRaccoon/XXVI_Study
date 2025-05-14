import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append('-1')
    elif cmd[0] == '3':
        output.append(str(len(stack)))
    elif cmd[0] == '4':
        output.append('1' if not stack else '0')
    elif cmd[0] == '5':
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append('-1')

print('\n'.join(output))
