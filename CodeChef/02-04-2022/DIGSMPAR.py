t = int(input())
for _ in range(t):
    n = input()
    t = int(n)
    if(t % 10 == 9):
        n = n[::-1]
        count = 0
        i = 0
        while(n[i] == '9'):
            count = count + 1
            i = i + 1
            if(i == len(n)):
                break
        if(count & 1 == 0):
            print(t + 1)
        else:
            print(t + 2)
    else:
        print(t + 1)
