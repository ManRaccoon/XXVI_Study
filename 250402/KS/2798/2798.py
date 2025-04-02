import sys
input = lambda : sys.stdin.readline()

N, M = map(int,input().split())

nums = list(map(int,input().split()))

max_sum = 0

for i in range(0,N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = nums[i] + nums[j] + nums[k]
            if (sum_num > max_sum) and (sum_num <= M):
                max_sum = sum_num

print(max_sum)
