t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if(b > a):
        temp = a
        a = b
        b = temp
    if(a - b == 2):
        print(1)
    elif (a - b == 1):
        if(a == n or b == 1):
            print(1)
        else:
            print(2)
    else:
        print(0)
