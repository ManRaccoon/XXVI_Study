import sys
input = lambda : sys.stdin.readline()
# 문자열 아닐땐 rstrip() 안써도 됨!
# ****꼭 lamda로 만들어서 쓸것 !!! ****

n,m = map(int,input().split())
a = []
b = []

for _ in range(n):
    nums = list(map(int,input().split()))
    a.append(nums)

for _ in range(n):
    nums = list(map(int,input().split()))
    b.append(nums)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j],end=" ")
    print()
