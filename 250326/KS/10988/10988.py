import sys
input = lambda : sys.stdin.readline().rstrip()

words = input()
flag = True

for i in range(len(words)):
    a = words[i]
    b = words[-1-i]
    if a != b :
        flag = False
        break

print(int(flag))
