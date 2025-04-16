import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

result = ['1' if num in cards else '0' for num in check]
print(' '.join(result))
