import sys
input = sys.stdin.readline
x=int(input())
num=[]
for _ in range(x):
  a=int(input())
  if a==0:
    num.pop()
  else:
    num.append(a)
print(sum(num))
