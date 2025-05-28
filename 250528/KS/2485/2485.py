import sys
import math
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]

diffs = [trees[i] - trees[i-1] for i in range(1, N)]

gcd = diffs[0]
for d in diffs[1:]:
    gcd = math.gcd(gcd, d)

total_new_trees = 0
for d in diffs:
    total_new_trees += (d // gcd - 1)

print(total_new_trees)
