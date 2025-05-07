import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

result = []
for t in targets:
    result.append('1' if t in cards else '0')

print(' '.join(result))
