t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if(m >= n):
        print(n)
    else:
        answer = m + ((n - m) * 2)
        print(answer)
