a=int(input())
b=[]
c=[]
for i in range(a):
  b.append(int(input()))
b.sort()
for i in range(a):
  c.append(b[i]*(len(b)-i))
print(max(c))
