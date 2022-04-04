t = int(input())
for _ in range(t):
    length, allowed = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    if(allowed >= length):
        print(arr[length - 1])
    else:
        print(arr[allowed])
