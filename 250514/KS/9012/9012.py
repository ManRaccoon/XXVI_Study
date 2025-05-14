import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    line = input().strip()
    stack = []
    is_vps = True

    for ch in line:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()
    
    if stack:
        is_vps = False

    result.append("YES" if is_vps else "NO")

print('\n'.join(result))
