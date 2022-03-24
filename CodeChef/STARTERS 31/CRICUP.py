T = int(input())
for i in range(T):
    x, y, d = map(int, input().split())
    if(y > x):
        x, y = y, x
    if((x - y) <= d):
        print('YES')
    else:
        print('NO')

'''
3
5 3 4
5 3 1
5 5 0
'''
