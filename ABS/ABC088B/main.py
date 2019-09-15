n = int(input())
nums = list(map(int, input().split()))
snums = sorted(nums, reverse=True)

a = 0
b = 0
for i in range(n):
    if (i % 2 == 0):
        a += snums[i]
    else:
        b += snums[i]
print(a-b)
