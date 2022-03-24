testCases = int(input())
arr = list()
for i in range(testCases):
    n = int(input())
    tempArr = list(map(int, input().split()))
    arr.append(tempArr)

for i in range(testCases):
    A = arr[i]

    flag = 1

    left = 0
    right = len(A) - 1

    curr = max(A[left], A[right])
    while(left < right):
        if(A[left] <= curr and A[right] <= curr):
            if(A[left] > A[right]):
                curr = A[left]
                left = left + 1
            else:
                curr = A[right]
                right = right - 1
        else:
            flag = 0
            break

    if(flag):
        print('Yes')
    else:
        print('No')
