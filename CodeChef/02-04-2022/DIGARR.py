t = int(input())
for _ in range(t):
    d = input()
    n = input()
    if(n.__contains__('0') or n.__contains__('5')):
        print('Yes')
    else:
        print('No')
