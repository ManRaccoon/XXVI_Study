import sys
input = lambda : sys.stdin.readline()

nums = []
for _ in range(5):
    nums.append(int(input()))
nums = sorted(nums)

print(sum(nums)//5)
print(nums[2])
