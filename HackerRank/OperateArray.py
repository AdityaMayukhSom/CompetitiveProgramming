T = int(input())
finalArr = list()
for i in range(T):
    int1, int2 = input().split()
    N = int(int1)
    K = int(int2)
    arr = list(map(int, input().split()))
    for count in range(K):
        maxArr = arr[0]
        for j in range(N):
            if(arr[j] > maxArr):
                maxArr = arr[j]
        for j in range(N):
            arr[j] = maxArr - arr[j]
    finalArr.append(arr)
for var1 in range(T):
    printArr = finalArr[var1]
    for var2 in range(len(printArr)):
        print(printArr[var2], end=' ')
    print()
