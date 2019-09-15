l = int(input())
nums = input().split()
c = 0

while all(int(n) % 2 == 0 for n in nums):
    nums = [int(n) / 2 for n in nums]
    c += 1

print(c)
