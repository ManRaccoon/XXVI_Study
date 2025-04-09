N = int(input())

result = 0

for i in range(1, N+1):
    digit_sum = sum(map(int, str(i)))
    if i + digit_sum == N:
        result = i
        break

print(result)
