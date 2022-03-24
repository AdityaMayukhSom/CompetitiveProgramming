T = int(input())
for i in range(T):
    n = int(input())
    if n & 1 == 1:
        position = -1 * ((n >> 1) + 1)
    else:
        position = n >> 1
    print(int(position))
