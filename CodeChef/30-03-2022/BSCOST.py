t = int(input())
for _ in range(t):
    s, x, y = map(int, input().split())
    n = input()
    if(n.__contains__('0') and n.__contains__('1')):
        print(min(x, y))
    else:
        print(0)
