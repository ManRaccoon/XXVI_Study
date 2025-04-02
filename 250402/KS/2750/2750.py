import sys
input = lambda : sys.stdin.readline()

n = int(input())
n_list = []
for _ in range(n):
    num = int(input())  # int로 바꾸고 append 하는거 한줄에 해도 됨.
    n_list.append(num)

n_list = sorted(n_list)
for sort_n in n_list:
    print(sort_n)
