T = int(input())
arr = list()
for i in range(T):
    arr.append(int(input()))


for number in arr:
    concat = ""
    while(number > 0):
        digit = number % 10
        number = int(number / 10)
        square = digit**2
        concat = str(square) + concat
    print(int(concat))
