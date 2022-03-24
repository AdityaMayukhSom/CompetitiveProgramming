T = int(input())
for i in range(T):
    n = int(input())
    upperNum = 1
    count = 0
    while(upperNum <= n):
        upperNum = upperNum << 1
        count = count + 1
    print(upperNum)
    number = (upperNum - count - 1) - (upperNum - n) + 1
    print(number)
