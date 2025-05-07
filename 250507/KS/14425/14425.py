import sys
input = sys.stdin.readline

N, M = map(int, input().split())
string_set = set(input().strip() for _ in range(N))

count = 0
for _ in range(M):
    query = input().strip()
    if query in string_set:
        count += 1

print(count)
