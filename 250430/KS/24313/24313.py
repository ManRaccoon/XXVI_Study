import sys

a,b = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

flag = 1
for i in range(n,101):
    if a*i+b > c*i :
        flag = 0
        break
print(flag)
