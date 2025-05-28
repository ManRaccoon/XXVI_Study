from collections import Counter

n = int(input())
A = list(map(int, input().split()))

freq = Counter(A)
result = [-1] * n
stack = []

for i in range(n):
    while stack and freq[A[i]] > freq[A[stack[-1]]]:
        idx = stack.pop()
        result[idx] = A[i]
    stack.append(i)

print(' '.join(map(str, result)))
