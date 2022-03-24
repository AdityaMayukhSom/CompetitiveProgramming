T = int(input())
arr = list() #Creating a list to take the numbers as input on which we have to check
for i in range(T):
    arr.append(int(input())) #Getting the numbers as input

#Now lets loop through arr and check if the number can be a 'SplitPair' or not
for i in range(T):
    evenDigit = 0
    oddDigit = 0
    zeroCount = 0
    num = arr[i]
    numList = list()

    # Taking the digits of the number in an array
    while(num > 0):
        numList.append(num % 10)
        num = int(num / 10)

    # Logic is that if the number contains either of atleast 2 even digit or atleast 2 odd digit, we can make a number ending with them, now as sum of both two odd or even is an even number, so the sum will be divisible by 2
    # There is a twist, if a number contains only one digit, and other zeroes, such as 10000000, it counts 0 as even number and prints YES but here we can not split it to make either two even number or two odd number, so for that reason we need to modify our code.


    #Counting the number of zeroes, evenDigits and oddDigits
    for i in numList:
        if i == 0:
            zeroCount = zeroCount+1
        else:
            if i%2 == 0:
                evenDigit = evenDigit+1
            else:
                oddDigit = oddDigit+1

    #Now here is our new logic, if we have atleast two odd or two even, then booah! we will print YES. 
    #But the tricky part is in cases like 1000 or 3400, for 1000 , we should print NO and for 3400, we should print YES.
    #now if we have atleast one zero, and the sum of evenDigit+oddDigit >= 2, that is if we have atleast one and one even digit, and atlease one zero, that is zeroCount>=1, we should also print YES.

    if((evenDigit>=2) or (oddDigit>=2) or (((oddDigit+evenDigit)>=2) and (zeroCount>=1))):
        print('YES')
    else:
        print('NO')