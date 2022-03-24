T = int(input())
for i in range(T):
    count = 0
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for j in range(n):
        if(s[j] == t[j]):
            count = count + 1
    print(count)
