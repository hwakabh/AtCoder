N, Y = list(map(int, input().split()))
# Y / 1000 = N + 9x + 4y
# 9x + 4y = Y / 1000 - N

s = Y // 1000 - N
for y in range(9):
    if (s - 4 * y) % 9 == 0:
        x = (s - 4 * y) // 9
        z = N - x - y
        if (x < 0) or (y < 0) or (z < 0):
            print("-1 -1 -1")
        else:
            print("{0} {1} {2}".format(x, y, z))

