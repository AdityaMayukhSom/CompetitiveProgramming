T = int(input())

for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    low, high = 1, 2
    count, subcount = 0, 0
    i = 0

    # Remember that in for loop, as range fives an iterator, it remembers the last position, so decreasing the value of i inside loop does not work

    while(i < n):
        if(arr[i] >= low and arr[i] < high):
            subcount = subcount + 1
            i = i + 1
        else:
            high = high * 2
            low = low * 2
            count = count + int((subcount * (subcount - 1)) / 2)
            subcount = 0

    # This is a security overhead, sometimes it can happen than subcount is not zero, and the while loop terminates without going to else first, in that case, this statement gets executed and it saves us.
    count = count + int((subcount * (subcount - 1)) / 2)
    print(count)
