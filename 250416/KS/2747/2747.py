n = int(input())

fib = [0, 1]  # F(0), F(1)

for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])

print(fib[n])
