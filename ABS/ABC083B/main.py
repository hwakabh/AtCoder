l, a, b = map(int, input().split())
s = 0
for i in range(1, l+1):
    sd = 0
    for j in str(i):
        sd += int(j)
    if (a <= sd) and (sd <= b):
        s += i

print(s)
