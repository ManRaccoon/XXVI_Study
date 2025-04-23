import sys
input = lambda: sys.stdin.readline()

N = int(input())
left, right = 0, N

while left <= right:
    mid = (left + right) // 2
    if mid * mid >= N:
        right = mid - 1
    else:
        left = mid + 1

print(left)
