T = int(input())
for i in range(T):
    n, x = map(int, input().split())
    roll = ((2 * n) + 1 - x)
    print(roll)
