import sys
input = sys.stdin.readline

N = int(input())
employees = set()

for _ in range(N):
    name, status = input().strip().split()
    if status == "enter":
        employees.add(name)
    else:
        employees.remove(name)

for name in sorted(employees, reverse=True):
    print(name)
