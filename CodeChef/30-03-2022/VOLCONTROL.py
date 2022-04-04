T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    if(x > y):
        answer = x - y
    else:
        answer = y - x
    print(answer)
