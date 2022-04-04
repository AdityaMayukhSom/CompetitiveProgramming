t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    oddCount = 0
    l1 = []
    for item in arr:
        if item not in l1:
            l1.append(item)
    for item in l1:
        count = arr.count(item)
        if(count & 1 == 1):
            oddCount = oddCount + 1
    value = n + oddCount
    if(value % 4 == 0):
        print(oddCount)
    else:
        print(oddCount + 2)
