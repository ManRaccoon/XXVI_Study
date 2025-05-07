n = int(input())
arr = list(map(int, input().split()))

pos = [0] * (n + 1)
for idx, num in enumerate(arr):
    pos[num] = idx

max_seq = 1
curr_len = 1

for i in range(2, n + 1):
    if pos[i - 1] < pos[i]:
        curr_len += 1
    else:
        curr_len = 1
    max_seq = max(max_seq, curr_len)

print(n - max_seq)
