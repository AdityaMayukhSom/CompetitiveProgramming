t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if(n + k <= m):
        print('Yes')
    else:
        print('No')
