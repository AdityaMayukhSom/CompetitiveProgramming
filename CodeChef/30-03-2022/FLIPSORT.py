t = int(input())
for _ in range(t):
    count = 0
    n = int(input())
    s = list(input())
    arr = list()
    left, right = 0, n - 1
    while(True):
        while(s[left] != '1'):
            left = left + 1
            if(left > right):
                break
        while(s[right] != '0'):
            right = right - 1
            if(left > right):
                break
        if(left > right):
            break
        count = count + 1
        arr.append([left + 1, right - left + 1])
        for temp in range(left, right + 1):
            if(s[temp] == '0'):
                s[temp] = '1'
            else:
                s[temp] = '0'

    print(len(arr))
    for p in range(len(arr)):
        print(arr[p][0], arr[p][1])
