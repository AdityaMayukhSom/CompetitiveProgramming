T = int(input())
for i in range(T):
    n = int(input())
    string = input()
    zero = 0
    one = 0
    for digit in string:
        if digit == '0':
            zero = zero + 1
        if digit == '1':
            one = one + 1
    atlease_length = (min(zero, one)) * 2
    if(zero != one):
        # If zero is not equal to one, we can assume there is atlease one extra 1 or 0 left to increase the length of the substring

        # eg 111100 here 1010 has length 4, but 2 more 1 remains, so alternative string can become 10101
        length = atlease_length + 1
    else:
        length = atlease_length

    print(length)
